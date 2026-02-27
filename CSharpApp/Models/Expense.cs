namespace CSharpApp.Models;

/// <summary>
/// Represents a single expense entry recorded by the application.
/// </summary>
public sealed class Expense
{
    /// <summary>
    /// Gets or sets the unique identifier for the expense entry.
    /// </summary>
    public Guid Id { get; set; }

    /// <summary>
    /// Gets or sets the date on which the expense occurred.
    /// </summary>
    public DateTime Date { get; set; }

    /// <summary>
    /// Gets or sets the category assigned to the expense.
    /// </summary>
    public string Category { get; set; } = string.Empty;

    /// <summary>
    /// Gets or sets an optional free-text description for the expense.
    /// </summary>
    public string Description { get; set; } = string.Empty;

    /// <summary>
    /// Gets or sets the monetary amount of the expense.
    /// </summary>
    public decimal Amount { get; set; }

    /// <summary>
    /// Creates a deep copy of the current <see cref="Expense"/> instance.
    /// </summary>
    public Expense Clone()
    {
        return new Expense
        {
            Id = Id,
            Date = Date,
            Category = Category,
            Description = Description,
            Amount = Amount
        };
    }

    public override string ToString()
    {
        return $"{Date:yyyy-MM-dd} | {Category} | {Amount:F2}";
    }
}
