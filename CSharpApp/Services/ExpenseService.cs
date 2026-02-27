using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using CSharpApp.Models;

namespace CSharpApp.Services;

/// <summary>
/// Implements the core business rules for managing expenses.
/// </summary>
public sealed class ExpenseService
{
    private readonly ExpenseRepository _repository;

    public ExpenseService(ExpenseRepository repository)
    {
        _repository = repository ?? throw new ArgumentNullException(nameof(repository));
    }

    /// <summary>
    /// Adds a new expense entry to the storage.
    /// </summary>
    public Expense AddExpense(DateTime date, string category, string description, decimal amount)
    {
        if (date == default)
        {
            throw new ArgumentException("The expense date must be provided.", nameof(date));
        }

        if (category is null)
        {
            throw new ArgumentNullException(nameof(category));
        }

        category = category.Trim();
        if (category.Length == 0)
        {
            throw new ArgumentException("The expense category cannot be empty.", nameof(category));
        }

        if (category.Length > 64)
        {
            throw new ArgumentException("The expense category cannot exceed 64 characters.", nameof(category));
        }

        description = (description ?? string.Empty).Trim();
        if (description.Length > 512)
        {
            throw new ArgumentException("The expense description cannot exceed 512 characters.", nameof(description));
        }

        if (amount <= 0)
        {
            throw new ArgumentOutOfRangeException(nameof(amount), amount, "The expense amount must be greater than zero.");
        }

        amount = decimal.Round(amount, 2, MidpointRounding.AwayFromZero);

        var expenses = _repository.Load();
        var expense = new Expense
        {
            Id = Guid.NewGuid(),
            Date = date.Date,
            Category = category,
            Description = description,
            Amount = amount
        };

        expenses.Add(expense);
        _repository.Save(expenses);

        return expense.Clone();
    }

    /// <summary>
    /// Retrieves all expenses that match the supplied filters.
    /// </summary>
    public IReadOnlyList<Expense> ListExpenses(
        DateTime? from = null,
        DateTime? to = null,
        IReadOnlyCollection<string>? categories = null)
    {
        if (from.HasValue && to.HasValue && from.Value.Date > to.Value.Date)
        {
            throw new ArgumentException("The 'from' date cannot be later than the 'to' date.");
        }

        var expenses = _repository.Load();
        return FilterExpenses(expenses, from, to, categories);
    }

    /// <summary>
    /// Removes the expense with the specified identifier from storage.
    /// </summary>
    public bool RemoveExpense(Guid id)
    {
        var expenses = _repository.Load();
        var removed = expenses.RemoveAll(expense => expense.Id == id) > 0;
        if (removed)
        {
            _repository.Save(expenses);
        }

        return removed;
    }

    /// <summary>
    /// Computes aggregate information for the stored expenses.
    /// </summary>
    public BudgetSummary GetSummary(
        DateTime? from = null,
        DateTime? to = null,
        IReadOnlyCollection<string>? categories = null)
    {
        if (from.HasValue && to.HasValue && from.Value.Date > to.Value.Date)
        {
            throw new ArgumentException("The 'from' date cannot be later than the 'to' date.");
        }

        var filtered = FilterExpenses(_repository.Load(), from, to, categories);
        var total = filtered.Sum(expense => expense.Amount);
        var count = filtered.Count;
        var average = count > 0 ? total / count : 0m;
        var largest = filtered.Count > 0 ? filtered.MaxBy(expense => expense.Amount)?.Clone() : null;

        var categoryTotals = filtered
            .GroupBy(expense => expense.Category, StringComparer.OrdinalIgnoreCase)
            .Select(group =>
            {
                var representative = group.OrderBy(expense => expense.Category, StringComparer.Ordinal).First();
                return new CategoryTotal(representative.Category, group.Sum(expense => expense.Amount));
            })
            .OrderBy(totalByCategory => totalByCategory.Category, StringComparer.OrdinalIgnoreCase)
            .ToList();

        return new BudgetSummary(total, average, largest, new ReadOnlyCollection<CategoryTotal>(categoryTotals), count);
    }

    private static List<Expense> FilterExpenses(
        List<Expense> source,
        DateTime? from,
        DateTime? to,
        IReadOnlyCollection<string>? categories)
    {
        if (source is null)
        {
            throw new ArgumentNullException(nameof(source));
        }

        IEnumerable<Expense> query = source.Select(expense => expense.Clone());

        if (from.HasValue)
        {
            var fromDate = from.Value.Date;
            query = query.Where(expense => expense.Date >= fromDate);
        }

        if (to.HasValue)
        {
            var toDate = to.Value.Date;
            query = query.Where(expense => expense.Date <= toDate);
        }

        if (categories is { Count: > 0 })
        {
            var categorySet = new HashSet<string>(categories, StringComparer.OrdinalIgnoreCase);
            query = query.Where(expense => categorySet.Contains(expense.Category));
        }

        return query
            .OrderBy(expense => expense.Date)
            .ThenBy(expense => expense.Category, StringComparer.OrdinalIgnoreCase)
            .ThenBy(expense => expense.Description, StringComparer.OrdinalIgnoreCase)
            .ToList();
    }
}
