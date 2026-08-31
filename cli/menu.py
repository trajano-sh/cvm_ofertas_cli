import os
from rich.console import Console
from utils.utils import banner

console = Console()

def menu():
    print(banner())
    menu=f"""
1) Filtrar por periodo
2) Abrir por id
0) Exit"""
    print(menu)
