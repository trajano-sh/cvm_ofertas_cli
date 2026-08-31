import os
from rich.console import Console

from config.config import BANNER_PATH
from utils.utils import banner

console = Console()


def show_menu():
    print(BANNER_PATH.read_text(encoding="utf-8"))
    options = """
1) Filtrar por período
2) Abrir por ID
3) Pesquisa detalhada
0) Sair
"""
    print(options)
