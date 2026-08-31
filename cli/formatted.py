from typing import Dict, Any, List
from rich.console import Console
from rich.table import Table
from rich.align import Align
from rich.console import Console
from rich.table import Table

from config.config import OFFER_URL
from utils.utils import console_ok

console = Console()

def cell(text: str, align: str = "left") -> Align:
    return Align(str(text), align=align, vertical="middle")

def print_rich_table(data: dict,dt_start:str,dt_end:str):
    console = Console()
    table = Table(title=f"Ofertas CVM {dt_start} - {dt_end}", show_lines=True)

    table.add_column("ID", justify="center", no_wrap=True)
    table.add_column("Emissor", justify="left")
    table.add_column("Valor (R$)", justify="right")
    table.add_column("Situação", justify="center")
    table.add_column("Tipo", justify="left")
    table.add_column("Tipo Requerimento", justify="left")

    registros = data.get("registros", [])
    if not registros:
        console.print("[yellow]Nenhum registro encontrado.[/yellow]")
        return

    for item in registros:
        table.add_row(
            cell(item.get("idRequerimento", "N/A"), align="center"),
            cell(item.get("nomeEmissor", "N/A"), align="left"),
            cell(item.get("valorTotalEmReais", "N/A"), align="right"),
            cell(item.get("statusDaOferta", "N/A"), align="center"),
            cell(item.get("nomeValorMobiliario", "N/A"), align="left"),
            cell(item.get("nomeTipoRequerimento", "N/A"), align="left")
        )

    console.print(table)

def parse_brl_to_float(val_str: str) -> float:
    if not val_str or not isinstance(val_str, str):
        return 0.0
    clean_val = val_str.replace(".", "").replace(",", ".")
    try:
        return float(clean_val)
    except ValueError:
        return 0.0

def format_get_offer(data: Dict[str, Any],ID:int) -> None:
    table = Table(title="Ofertas CVM", show_lines=True,show_header=False)

    table.add_column("Campo",justify="left")
    table.add_column("Valor",justify="left")

    table.add_row(
        Align.center("[bold yellow]PARÂMETRO[/bold yellow]"),
        Align.center("[bold yellow]VALOR[/bold yellow]"),
        end_section=True
    )
    table.add_row("Processo",f"{data.get("numeroProcesso")}")
    table.add_row("Tipo de oferta",f"{data.get("nomeValorMobiliario")}")
    table.add_row("Valor",f"{data.get("valorTotal")}")
    table.add_row("Data",f"{data.get("data")}")
    table.add_row("Link",f"{OFFER_URL}{ID}")
    console.print(table)
    console_ok("Offert found")
    input("Pressione Enter para continuar...")

def print_offers_table(offers: list[dict]) -> None:
    table = Table(title="Ofertas CVM")

    table.add_column("ID", justify="center", no_wrap=True)
    table.add_column("Emissor")
    table.add_column("CNPJ")
    table.add_column("Tipo")
    table.add_column("Valor")
    table.add_column("Data")
    for offer in offers:
        table.add_row(
            offer.get("Numero_Requerimento", "N/A"),
            offer.get("Nome_Emissor", "N/A"),
            offer.get("CNPJ_Emissor", "N/A"),
            offer.get("Tipo_Oferta", "N/A"),
            offer.get("Valor_Total_Registrado", "N/A"),
            offer.get("Data_requerimento", "N/A"),
        )

    console.print(table)