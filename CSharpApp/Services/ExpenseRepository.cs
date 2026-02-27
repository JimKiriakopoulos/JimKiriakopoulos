using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using CSharpApp.Models;

namespace CSharpApp.Services;

/// <summary>
/// Provides a simple JSON based persistence layer for <see cref="Expense"/> entities.
/// </summary>
public sealed class ExpenseRepository
{
    private static readonly JsonSerializerOptions SerializerOptions = new()
    {
        WriteIndented = true,
        PropertyNameCaseInsensitive = true
    };

    private readonly object _syncRoot = new();
    private readonly string _storagePath;

    public ExpenseRepository(string storagePath)
    {
        if (string.IsNullOrWhiteSpace(storagePath))
        {
            throw new ArgumentException("The storage path cannot be empty.", nameof(storagePath));
        }

        _storagePath = storagePath;
        var directory = Path.GetDirectoryName(storagePath);
        if (!string.IsNullOrEmpty(directory))
        {
            Directory.CreateDirectory(directory);
        }
    }

    /// <summary>
    /// Retrieves all expenses from the storage.
    /// </summary>
    public List<Expense> Load()
    {
        lock (_syncRoot)
        {
            try
            {
                if (!File.Exists(_storagePath))
                {
                    return new List<Expense>();
                }

                var json = File.ReadAllText(_storagePath);
                if (string.IsNullOrWhiteSpace(json))
                {
                    return new List<Expense>();
                }

                var expenses = JsonSerializer.Deserialize<List<Expense?>>(json, SerializerOptions) ?? new List<Expense?>();
                return expenses
                    .Where(expense => expense is not null)
                    .Select(expense => Sanitize(expense!))
                    .ToList();
            }
            catch (JsonException ex)
            {
                throw new InvalidOperationException($"The storage file '{_storagePath}' does not contain valid JSON data.", ex);
            }
            catch (IOException ex)
            {
                throw new InvalidOperationException($"Unable to read the storage file '{_storagePath}'.", ex);
            }
        }
    }

    /// <summary>
    /// Persists the supplied expense collection to storage.
    /// </summary>
    public void Save(IEnumerable<Expense> expenses)
    {
        if (expenses is null)
        {
            throw new ArgumentNullException(nameof(expenses));
        }

        var payload = expenses
            .Where(expense => expense is not null)
            .Select(expense => Sanitize(expense))
            .ToList();

        lock (_syncRoot)
        {
            try
            {
                var json = JsonSerializer.Serialize(payload, SerializerOptions);
                File.WriteAllText(_storagePath, json);
            }
            catch (IOException ex)
            {
                throw new InvalidOperationException($"Unable to write to the storage file '{_storagePath}'.", ex);
            }
        }
    }

    private static Expense Sanitize(Expense expense)
    {
        if (expense is null)
        {
            throw new ArgumentNullException(nameof(expense));
        }

        var clone = expense.Clone();
        if (clone.Id == Guid.Empty)
        {
            clone.Id = Guid.NewGuid();
        }

        clone.Category = (clone.Category ?? string.Empty).Trim();
        clone.Description = (clone.Description ?? string.Empty).Trim();
        clone.Date = clone.Date == default ? DateTime.Today : clone.Date.Date;
        clone.Amount = decimal.Round(clone.Amount, 2, MidpointRounding.AwayFromZero);
        return clone;
    }
}
