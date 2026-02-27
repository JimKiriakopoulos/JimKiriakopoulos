# Expense Tracker CLI

A lightweight command-line application for recording and analysing personal expenses. By default, data is persisted as JSON inside the `CSharpApp/data` folder (relative to the project file). The project targets .NET 8 and does not require any external dependencies.

## Building and running

```bash
# Build the project (requires the .NET SDK to be installed)
dotnet build CSharpApp/CSharpApp.csproj

# Run a command (note the `--` to separate CLI options from `dotnet`)
dotnet run --project CSharpApp -- <command> [options]
```

## Available commands

- `add` – records a new expense (requires `--date`, `--category`, and `--amount`).
- `list` – displays the recorded expenses and accepts filters such as `--from`, `--to`, and `--category`.
- `summary` – produces aggregate information (total, average, and per-category totals).
- `remove` – removes an expense by its identifier (`--id`).
- `help` – shows the usage information.

The CLI accepts options either as `--name value` or `--name=value`. Unknown options are rejected per command to catch typos early.

## Storage

At runtime the application looks for the `CSharpApp.csproj` file and stores entries in `data/expenses.json` next to it. When the project file cannot be located (for example, after publishing a self-contained executable) the data file falls back to `<app base>/data/expenses.json`. You can override the location entirely by setting the `EXPENSE_TRACKER_STORAGE` environment variable to an absolute or relative file path before running the program. The generated data file is ignored by Git so that runtime changes do not pollute the repository history.
