using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CSharpApp.Utilities;

/// <summary>
/// Provides helper methods for rendering collections as text tables.
/// </summary>
public static class TableFormatter
{
    public static string Format(IEnumerable<IReadOnlyList<string>> rows)
    {
        if (rows is null)
        {
            throw new ArgumentNullException(nameof(rows));
        }

        var normalizedRows = rows
            .Select(row => row?.Select(cell => cell ?? string.Empty).ToArray() ?? Array.Empty<string>())
            .ToList();

        if (normalizedRows.Count == 0)
        {
            return string.Empty;
        }

        var columnCount = normalizedRows.Max(row => row.Length);
        var widths = new int[columnCount];

        foreach (var row in normalizedRows)
        {
            for (var column = 0; column < row.Length; column++)
            {
                widths[column] = Math.Max(widths[column], row[column].Length);
            }
        }

        var builder = new StringBuilder();
        for (var index = 0; index < normalizedRows.Count; index++)
        {
            builder.AppendLine(FormatRow(normalizedRows[index], widths));

            if (index == 0)
            {
                builder.AppendLine(FormatDivider(widths));
            }
        }

        return builder.ToString().TrimEnd();
    }

    public static IReadOnlyList<string> Row(params string[] values)
    {
        return values ?? Array.Empty<string>();
    }

    private static string FormatRow(IReadOnlyList<string> row, IReadOnlyList<int> widths)
    {
        var cells = new string[widths.Count];
        for (var column = 0; column < widths.Count; column++)
        {
            var value = column < row.Count ? row[column] : string.Empty;
            cells[column] = (value ?? string.Empty).PadRight(widths[column]);
        }

        return string.Join("  ", cells);
    }

    private static string FormatDivider(IReadOnlyList<int> widths)
    {
        var cells = new string[widths.Count];
        for (var column = 0; column < widths.Count; column++)
        {
            var width = Math.Max(1, widths[column]);
            cells[column] = new string('-', width);
        }

        return string.Join("  ", cells);
    }
}
