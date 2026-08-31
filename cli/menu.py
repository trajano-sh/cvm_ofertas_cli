import os
from rich.console import Console
from utils.utils import banner

console = Console()

def show_menu():
    print(banner())
    options = """
1) Filtrar por período
2) Abrir por ID
3) Pesquisa detalhada
0) Sair
"""
    print(options)