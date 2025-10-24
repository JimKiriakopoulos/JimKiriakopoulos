namespace CSharpApp.Models;

/// <summary>
/// Represents the aggregated amount spent within a specific expense category.
/// </summary>
public sealed record CategoryTotal(string Category, decimal Amount);
