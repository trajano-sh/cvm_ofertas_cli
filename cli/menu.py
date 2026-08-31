import os
from dotenv import load_dotenv
from rich.console import Console

console = Console()

load_dotenv()
VERSION = os.getenv("VERSION")
BANNER = F"""[blue]   _____   ____  __    ___  ___ ___ ___ _____ _   ___ 
  / __\ \ / /  \/  |  / _ \| __| __| _ \_   _/_\ / __|
 | (__ \ V /| |\/| | | (_) | _|| _||   / | |/ _ \\__ \\
  \___| \_/ |_|  |_|  \___/|_| |___|_|_\ |_/_/ \_\___/[/blue]
{VERSION}
"""

def menu():
    console.print(BANNER)
    menu=f"""
1) Filtrar por periodo
2) Abrir por id
0) Exit"""
    print(menu)