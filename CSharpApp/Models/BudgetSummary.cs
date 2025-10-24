namespace CSharpApp.Models;

/// <summary>
/// Provides a high level overview of the stored expense information.
/// </summary>
public sealed class BudgetSummary
{
    public BudgetSummary(
        decimal totalSpent,
        decimal averageExpense,
        Expense? largestExpense,
        IReadOnlyList<CategoryTotal> categoryTotals,
        int expenseCount)
    {
        if (categoryTotals is null)
        {
            throw new ArgumentNullException(nameof(categoryTotals));
        }

        TotalSpent = totalSpent;
        AverageExpense = averageExpense;
        LargestExpense = largestExpense;
        CategoryTotals = categoryTotals;
        ExpenseCount = expenseCount;
    }

    /// <summary>
    /// Gets the total amount spent for the selected time frame.
    /// </summary>
    public decimal TotalSpent { get; }

    /// <summary>
    /// Gets the average amount of the expenses that form the summary.
    /// </summary>
    public decimal AverageExpense { get; }

    /// <summary>
    /// Gets the largest expense contributing to the summary, if any.
    /// </summary>
    public Expense? LargestExpense { get; }

    /// <summary>
    /// Gets the ordered collection of category totals.
    /// </summary>
    public IReadOnlyList<CategoryTotal> CategoryTotals { get; }

    /// <summary>
    /// Gets the number of expense entries considered while building the summary.
    /// </summary>
    public int ExpenseCount { get; }
}
