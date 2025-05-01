import csv
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from datetime import timedelta

# Helper to convert HH:MM:SS to seconds
def time_to_seconds(t):
    h, m, s = map(int, t.split(":"))
    return h * 3600 + m * 60 + s

# Helper to format seconds to HH:MM:SS
def format_seconds(seconds):
    return str(timedelta(seconds=seconds))

def load_data(csv_path):
    data = []
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def summarize_by_category(data):
    summary = {}
    for row in data:
        category = row.get("Category", "Uncategorized")
        seconds = time_to_seconds(row["Elapsed Time"])
        summary.setdefault(category, {"total": 0, "tasks": []})
        summary[category]["total"] += seconds
        summary[category]["tasks"].append(row)
    return summary

def show_main_dashboard(summary):
    table = Table(title="⏱️ Time Summary by Category")

    table.add_column("Category", style="cyan", no_wrap=True)
    table.add_column("Total Time", justify="right", style="green")
    table.add_column("Tasks", justify="right", style="magenta")

    for cat, info in summary.items():
        table.add_row(cat, format_seconds(info["total"]), str(len(info["tasks"])))

    console.print(table)

def show_tasks_in_category(category, tasks):
    table = Table(title=f"📋 Tasks in {category}", show_lines=True)

    table.add_column("Date", style="dim", no_wrap=True)
    table.add_column("Task", style="white")
    table.add_column("Elapsed", justify="right", style="green")

    for task in tasks:
        table.add_row(task["Date and Time"], task["Task Name"], task["Elapsed Time"])

    console.print(table)

# Main logic
if __name__ == "__main__":
    console = Console()
    path = "categorized_data.csv"

    data = load_data(path)
    summary = summarize_by_category(data)

    show_main_dashboard(summary)

    while True:
        category = Prompt.ask("\nEnter a category to explore (or 'q' to quit)")
        if category.lower() == 'q':
            break
        elif category in summary:
            show_tasks_in_category(category, summary[category]["tasks"])
        else:
            console.print("[red]Category not found. Try again.[/red]")
