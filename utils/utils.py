import os

from rich.console import Console

console = Console()


def clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def console_error(message: str) -> None:
    console.print(f"[[red]ERRO[/red]] {message}")


def console_ok(message: str) -> None:
    console.print(f"[[green]OK[/green]] {message}")


def console_warn(message: str) -> None:
    console.print(f"[[yellow]AVISO[/yellow]] {message}")
