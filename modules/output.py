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

def workspace_tree(domain):
    tree = Tree("[bold cyan]results[/bold cyan]")
    target = tree.add(f"[green]{domain}[/green]")
    target.add("report.md")
    target.add("logs.txt")
    target.add("raw/")
    console.print(tree)
