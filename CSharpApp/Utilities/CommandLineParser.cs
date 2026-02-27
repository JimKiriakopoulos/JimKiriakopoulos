using System.Collections.Generic;

namespace CSharpApp.Utilities;

/// <summary>
/// Lightweight parser that converts CLI arguments into a command name and option dictionary.
/// </summary>
public static class CommandLineParser
{
    public static CommandLineInput Parse(string[] args)
    {
        if (args is null)
        {
            throw new ArgumentNullException(nameof(args));
        }

        if (args.Length == 0)
        {
            return new CommandLineInput("help", new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase));
        }

        var command = (args[0] ?? string.Empty).Trim();
        if (command.Length == 0)
        {
            command = "help";
        }

        var options = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
        for (var index = 1; index < args.Length; index++)
        {
            var token = args[index] ?? string.Empty;
            if (!token.StartsWith("--", StringComparison.Ordinal))
            {
                throw new ArgumentException($"Unexpected token '{token}'. Options must start with \"--\".");
            }

            var optionToken = token[2..];
            var equalsIndex = optionToken.IndexOf('=');

            string key;
            string? inlineValue = null;
            if (equalsIndex >= 0)
            {
                key = optionToken[..equalsIndex];
                inlineValue = optionToken[(equalsIndex + 1)..];
            }
            else
            {
                key = optionToken;
            }

            if (string.IsNullOrWhiteSpace(key))
            {
                throw new ArgumentException("Option names cannot be empty.");
            }

            if (options.ContainsKey(key))
            {
                throw new ArgumentException($"The option '--{key}' was specified more than once.");
            }

            string value;
            if (inlineValue is not null)
            {
                value = inlineValue;
            }
            else if (index + 1 < args.Length && !args[index + 1].StartsWith("--", StringComparison.Ordinal))
            {
                value = args[++index];
            }
            else
            {
                value = "true";
            }

            options[key] = value;
        }

        return new CommandLineInput(command, options);
    }
}

public sealed record CommandLineInput(string Command, IReadOnlyDictionary<string, string> Options);
