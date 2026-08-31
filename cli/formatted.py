from __future__ import annotations

from typing import Any

from rich.align import Align
from rich.console import Console
from rich.table import Table

from config.config import OFFER_URL
from utils.utils import console_ok, console_warn

console = Console()


def cell(value: Any, align: str = "left") -> Align:
    return Align(str(value if value not in (None, "") else "N/A"), align=align, vertical="middle")


def print_rich_table(data: dict[str, Any], date_start: str, date_end: str) -> bool:
    records = data.get("registros", []) if isinstance(data, dict) else []
    if not records:
        console_warn("Nenhum registro encontrado.")
        return False

    table = Table(title=f"Ofertas CVM {date_start or 'padrão'} - {date_end or 'hoje'}", show_lines=True)
    for label, justify in (("ID", "center"), ("Emissor", "left"), ("Valor (R$)", "right"), ("Situação", "center"), ("Tipo", "left"), ("Tipo Requerimento", "left")):
        table.add_column(label, justify=justify, no_wrap=label == "ID")
    for item in records:
        table.add_row(
            cell(item.get("idRequerimento"), "center"), cell(item.get("nomeEmissor")),
            cell(item.get("valorTotalEmReais"), "right"), cell(item.get("statusDaOferta"), "center"),
            cell(item.get("nomeValorMobiliario")), cell(item.get("nomeTipoRequerimento")),
        )
    console.print(table)
    return True


def format_get_offer(data: dict[str, Any], offer_id: str | int) -> None:
    table = Table(title="Oferta CVM", show_lines=True, show_header=False)
    table.add_column("Campo")
    table.add_column("Valor")
    table.add_row(Align.center("[bold yellow]PARÂMETRO[/bold yellow]"), Align.center("[bold yellow]VALOR[/bold yellow]"), end_section=True)
    for label, key in (("Processo", "numeroProcesso"), ("Tipo de oferta", "nomeValorMobiliario"), ("Valor", "valorTotal"), ("Data", "data")):
        table.add_row(label, str(data.get(key) or "N/A"))
    table.add_row("Link", f"{OFFER_URL}{offer_id}")
    console.print(table)
    console_ok("Oferta encontrada.")


def print_offers_table(offers: list[dict[str, str]]) -> bool:
    if not offers:
        console_warn("Nenhuma oferta encontrada.")
        return False
    table = Table(title=f"Ofertas CVM ({len(offers)} resultados)")
    for label in ("ID", "Emissor", "CNPJ", "Tipo", "Valor", "Data"):
        table.add_column(label, justify="center" if label == "ID" else "left", no_wrap=label == "ID")
    for offer in offers:
        table.add_row(*(offer.get(key) or "N/A" for key in ("Numero_Requerimento", "Nome_Emissor", "CNPJ_Emissor", "Tipo_Oferta", "Valor_Total_Registrado", "Data_requerimento")))
    console.print(table)
    return True
