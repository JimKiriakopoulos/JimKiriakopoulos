using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using CSharpApp.Services;
using CSharpApp.Utilities;

namespace CSharpApp;

internal static class Program
{
    private const string DateFormat = "yyyy-MM-dd";
    private const string ExecutionHint = "dotnet run --project CSharpApp --";

    private static void Main(string[] args)
    {
        if (args.Length == 0 || IsHelpRequest(args[0]))
        {
            PrintHelp();
            return;
        }

        var storagePath = ResolveStoragePath();
        var repository = new ExpenseRepository(storagePath);
        var service = new ExpenseService(repository);

        try
        {
            var commandInput = CommandLineParser.Parse(args);
            switch (commandInput.Command.ToLowerInvariant())
            {
                case "add":
                    HandleAdd(service, commandInput);
                    break;
                case "list":
                    HandleList(service, commandInput);
                    break;
                case "summary":
                    HandleSummary(service, commandInput);
                    break;
                case "remove":
                    HandleRemove(service, commandInput);
                    break;
                case "help":
                    PrintHelp();
                    break;
                default:
                    Console.Error.WriteLine($"Unknown command '{commandInput.Command}'.");
                    Console.Error.WriteLine();
                    PrintHelp();
                    Environment.ExitCode = 1;
                    break;
            }
        }
        catch (Exception ex) when (ex is ArgumentException or InvalidOperationException or FormatException)
        {
            Console.Error.WriteLine($"Error: {ex.Message}");
            Environment.ExitCode = 1;
        }
    }

    private static bool IsHelpRequest(string value)
    {
        return string.Equals(value, "-h", StringComparison.OrdinalIgnoreCase)
            || string.Equals(value, "--help", StringComparison.OrdinalIgnoreCase)
            || string.Equals(value, "help", StringComparison.OrdinalIgnoreCase);
    }

    private static void HandleAdd(ExpenseService service, CommandLineInput input)
    {
        var date = GetRequiredDate(input, "date");
        var category = GetRequiredString(input, "category");
        var amount = GetRequiredDecimal(input, "amount");
        var description = GetOptionalString(input, "description") ?? string.Empty;

        var expense = service.AddExpense(date, category, description, amount);

        Console.WriteLine("Expense recorded successfully:");
        Console.WriteLine($"  Id          : {expense.Id}");
        Console.WriteLine($"  Date        : {expense.Date.ToString(DateFormat, CultureInfo.InvariantCulture)}");
        Console.WriteLine($"  Category    : {expense.Category}");
        Console.WriteLine($"  Amount      : {expense.Amount.ToString("F2", CultureInfo.InvariantCulture)}");
        if (!string.IsNullOrWhiteSpace(expense.Description))
        {
            Console.WriteLine($"  Description : {expense.Description}");
        }
    }

    private static void HandleList(ExpenseService service, CommandLineInput input)
    {
        var from = GetOptionalDate(input, "from");
        var to = GetOptionalDate(input, "to");
        var categories = GetOptionalCategories(input);

        var expenses = service.ListExpenses(from, to, categories);
        if (expenses.Count == 0)
        {
            Console.WriteLine("No expenses found for the specified filters.");
            return;
        }

        var rows = new List<IReadOnlyList<string>>
        {
            TableFormatter.Row("Id", "Date", "Category", "Amount", "Description")
        };

        foreach (var expense in expenses)
        {
            rows.Add(TableFormatter.Row(
                expense.Id.ToString(),
                expense.Date.ToString(DateFormat, CultureInfo.InvariantCulture),
                expense.Category,
                expense.Amount.ToString("F2", CultureInfo.InvariantCulture),
                string.IsNullOrWhiteSpace(expense.Description) ? "-" : expense.Description));
        }

        Console.WriteLine(TableFormatter.Format(rows));
    }

    private static void HandleSummary(ExpenseService service, CommandLineInput input)
    {
        var from = GetOptionalDate(input, "from");
        var to = GetOptionalDate(input, "to");
        var categories = GetOptionalCategories(input);

        var summary = service.GetSummary(from, to, categories);
        if (summary.ExpenseCount == 0)
        {
            Console.WriteLine("No expenses found for the specified filters.");
            return;
        }

        Console.WriteLine("Summary");
        Console.WriteLine("-------");
        Console.WriteLine($"Entries        : {summary.ExpenseCount}");
        Console.WriteLine($"Total spent    : {summary.TotalSpent.ToString("F2", CultureInfo.InvariantCulture)}");
        Console.WriteLine($"Average amount : {summary.AverageExpense.ToString("F2", CultureInfo.InvariantCulture)}");

        if (summary.LargestExpense is { } largest)
        {
            Console.WriteLine();
            Console.WriteLine("Largest expense");
            Console.WriteLine($"  Id       : {largest.Id}");
            Console.WriteLine($"  Date     : {largest.Date.ToString(DateFormat, CultureInfo.InvariantCulture)}");
            Console.WriteLine($"  Category : {largest.Category}");
            Console.WriteLine($"  Amount   : {largest.Amount.ToString("F2", CultureInfo.InvariantCulture)}");
            if (!string.IsNullOrWhiteSpace(largest.Description))
            {
                Console.WriteLine($"  Notes    : {largest.Description}");
            }
        }

        if (summary.CategoryTotals.Count > 0)
        {
            Console.WriteLine();
            Console.WriteLine("Totals by category");
            var rows = new List<IReadOnlyList<string>>
            {
                TableFormatter.Row("Category", "Total")
            };

            foreach (var categoryTotal in summary.CategoryTotals)
            {
                rows.Add(TableFormatter.Row(
                    categoryTotal.Category,
                    categoryTotal.Amount.ToString("F2", CultureInfo.InvariantCulture)));
            }

            Console.WriteLine(TableFormatter.Format(rows));
        }
    }

    private static void HandleRemove(ExpenseService service, CommandLineInput input)
    {
        var id = GetRequiredGuid(input, "id");
        var removed = service.RemoveExpense(id);
        if (removed)
        {
            Console.WriteLine("Expense removed successfully.");
        }
        else
        {
            Console.WriteLine("No expense was found with the provided identifier.");
            Environment.ExitCode = 1;
        }
    }

    private static string ResolveStoragePath()
    {
        var overridePath = Environment.GetEnvironmentVariable("EXPENSE_TRACKER_STORAGE");
        if (!string.IsNullOrWhiteSpace(overridePath))
        {
            return Path.GetFullPath(overridePath);
        }

        var baseDirectory = AppContext.BaseDirectory;
        var projectRoot = TryResolveProjectRoot(baseDirectory);
        var dataDirectory = projectRoot is not null
            ? Path.Combine(projectRoot, "data")
            : Path.Combine(baseDirectory, "data");

        return Path.Combine(dataDirectory, "expenses.json");
    }

    private static string? TryResolveProjectRoot(string startDirectory)
    {
        if (string.IsNullOrWhiteSpace(startDirectory))
        {
            return null;
        }

        var current = new DirectoryInfo(startDirectory);
        while (current is not null)
        {
            var projectFile = Path.Combine(current.FullName, "CSharpApp.csproj");
            if (File.Exists(projectFile))
            {
                return current.FullName;
            }

            current = current.Parent;
        }

        return null;
    }

    private static DateTime GetRequiredDate(CommandLineInput input, string name)
    {
        if (!input.Options.TryGetValue(name, out var raw))
        {
            throw new ArgumentException($"The option '--{name}' is required for the '{input.Command}' command.");
        }

        return ParseDate(raw, name);
    }

    private static DateTime? GetOptionalDate(CommandLineInput input, string name)
    {
        if (!input.Options.TryGetValue(name, out var raw)
            || string.IsNullOrWhiteSpace(raw)
            || string.Equals(raw, "true", StringComparison.OrdinalIgnoreCase))
        {
            return null;
        }

        return ParseDate(raw, name);
    }

    private static DateTime ParseDate(string value, string name)
    {
        if (!DateTime.TryParseExact(value, DateFormat, CultureInfo.InvariantCulture, DateTimeStyles.None, out var date))
        {
            throw new FormatException($"The value '{value}' is not a valid date for the '--{name}' option. Use the format {DateFormat}.");
        }

        return date.Date;
    }

    private static decimal GetRequiredDecimal(CommandLineInput input, string name)
    {
        if (!input.Options.TryGetValue(name, out var raw))
        {
            throw new ArgumentException($"The option '--{name}' is required for the '{input.Command}' command.");
        }

        if (!decimal.TryParse(raw, NumberStyles.Float, CultureInfo.InvariantCulture, out var value))
        {
            throw new FormatException($"The value '{raw}' is not a valid number for the '--{name}' option.");
        }

        return value;
    }

    private static string GetRequiredString(CommandLineInput input, string name)
    {
        if (!input.Options.TryGetValue(name, out var raw)
            || string.IsNullOrWhiteSpace(raw)
            || string.Equals(raw, "true", StringComparison.OrdinalIgnoreCase))
        {
            throw new ArgumentException($"The option '--{name}' is required for the '{input.Command}' command.");
        }

        return raw.Trim();
    }

    private static string? GetOptionalString(CommandLineInput input, string name)
    {
        if (!input.Options.TryGetValue(name, out var raw)
            || string.IsNullOrWhiteSpace(raw)
            || string.Equals(raw, "true", StringComparison.OrdinalIgnoreCase))
        {
            return null;
        }

        return raw.Trim();
    }

    private static Guid GetRequiredGuid(CommandLineInput input, string name)
    {
        if (!input.Options.TryGetValue(name, out var raw))
        {
            throw new ArgumentException($"The option '--{name}' is required for the '{input.Command}' command.");
        }

        if (!Guid.TryParse(raw, out var id))
        {
            throw new FormatException($"The value '{raw}' is not a valid identifier for the '--{name}' option.");
        }

        return id;
    }

    private static IReadOnlyCollection<string>? GetOptionalCategories(CommandLineInput input)
    {
        if (!input.Options.TryGetValue("category", out var raw)
            || string.IsNullOrWhiteSpace(raw)
            || string.Equals(raw, "true", StringComparison.OrdinalIgnoreCase))
        {
            return null;
        }

        var categories = raw
            .Split(',', StringSplitOptions.RemoveEmptyEntries)
            .Select(category => category.Trim())
            .Where(category => category.Length > 0)
            .Distinct(StringComparer.OrdinalIgnoreCase)
            .ToList();

        return categories.Count > 0 ? categories : null;
    }

    private static void PrintHelp()
    {
        Console.WriteLine("Expense Tracker CLI");
        Console.WriteLine("===================");
        Console.WriteLine("Manage your personal expenses from the command line.");
        Console.WriteLine();
        Console.WriteLine("Usage examples:");
        Console.WriteLine($"  {ExecutionHint} add --date 2024-05-23 --category Food --amount 12.50 --description \"Lunch\"");
        Console.WriteLine($"  {ExecutionHint} list --from 2024-05-01 --to 2024-05-31");
        Console.WriteLine($"  {ExecutionHint} summary --category Food,Travel");
        Console.WriteLine($"  {ExecutionHint} remove --id <expense-id>");
        Console.WriteLine();
        Console.WriteLine("Commands:");
        Console.WriteLine("  add       Adds a new expense to the tracker.");
        Console.WriteLine("           Required options: --date yyyy-MM-dd, --category <name>, --amount <value>");
        Console.WriteLine("  list      Displays expenses. Optional options: --from yyyy-MM-dd, --to yyyy-MM-dd, --category name1,name2");
        Console.WriteLine("  summary   Provides aggregate information. Shares the optional filters from the list command.");
        Console.WriteLine("  remove    Deletes an expense using its identifier. Requires --id <guid>.");
        Console.WriteLine("  help      Displays this screen.");
    }
}
