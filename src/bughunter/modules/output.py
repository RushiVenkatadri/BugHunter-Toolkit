from rich.console import Console
from pathlib import Path
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

    root = Path("results") / domain

    tree = Tree("[bold cyan]results[/bold cyan]")

    target = tree.add(f"[green]{domain}[/green]")

    for item in sorted(root.iterdir()):

        if item.is_file():

            target.add(item.name)

        elif item.is_dir():

            directory = target.add(item.name)

            for child in sorted(item.iterdir()):

                directory.add(child.name)

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
