from rich.console import Console
from rich.tree import Tree

console = Console()

def success(message):
    console.print(f"[green][+][/green] {message}")

def info(message):
    console.print(f"[cyan][*][/cyan] {message}")

def warning(message):
    console.print(f"[yellow][!][/yellow] {message}")

def error(message):
    console.print(f"[red][-][/red] {message}")

def key_value(key, value):
    console.print(f"[bold cyan]{key:<16}[/bold cyan] {value}")

def workspace_tree(domain):
    tree = Tree("[bold cyan]results[/bold cyan]")
    target = tree.add(f"[green]{domain}[/green]")
    target.add("report.md")
    target.add("logs.txt")
    target.add("raw/")
    console.print(tree)
def security_report(findings):

    console.print("\n[bold magenta]Security Headers[/bold magenta]")

    for item in findings:

        if item["status"] == "Present":
            console.print(
                f"[green]✓[/green] {item['description']}"
            )

        else:
            console.print(
                f"[red]✗[/red] {item['description']}"
            )
