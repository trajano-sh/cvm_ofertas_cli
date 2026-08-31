from typing import Dict, Any, List
from rich.console import Console
from rich.table import Table
from rich.align import Align

from rich.console import Console
from rich.table import Table

from rich.console import Console
from rich.table import Table
from rich.align import Align

def cell(text: str, align: str = "left") -> Align:
    return Align(str(text), align=align, vertical="middle")

def print_rich_table(data: dict):
    console = Console()
    table = Table(title="Ofertas CVM", show_lines=True)

    # Definição das colunas
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

def format_get_offer(data: Dict[str, Any],id:int) -> None:
    print(f"Processo: {data.get("numeroProcesso")}")
    print(f"Tipo de Oferta: {data.get("nomeValorMobiliario")}")
    print(f"Valor: {data.get("valorTotal")}")
    print(f"Data: {data.get("data")}")
    print(f"link: https://web.cvm.gov.br/sre-publico-cvm/#/oferta-publica/{id}")
