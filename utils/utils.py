import os
from rich.console import Console
from config.config import BANNER_PATH

console = Console()

WARN = "[[yellow]WARN[/yellow]]"
ERROR = "[[red]ERROR[/red]]"
OK = "[[green]OK[/green]]"

def banner()->str:
    clear()
    with open(BANNER_PATH,"r",encoding="utf-8") as banner_:
        banner_ = banner_.read()
    return banner_

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def console_error(self:str):
    console.print(f"{ERROR} {self}")

def console_ok(self: str):
    console.print(f"{OK} {self}")

def console_warn(self: str):
    console.print(f"{WARN} {self}")