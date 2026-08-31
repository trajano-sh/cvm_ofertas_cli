from __future__ import annotations

from pathlib import Path
from typing import Any

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

from config.config import OFFER_URL, ROOT_DIR
from utils.utils import console_ok

HEADERS = ("ID", "NOME EMISSOR", "CNPJ EMISSOR", "NOME COORDENADOR LÍDER", "CNPJ COORDENADOR LÍDER", "TIPO REQUERIMENTO", "TIPO DE OFERTA", "STATUS", "NÚMERO PROCESSO", "NÚMERO REGISTRO", "VALOR EM REAIS", "POSSUI BOOK", "DATA", "LINK")
FIELDS = ("idRequerimento", "nomeEmissor", "cnpjEmissor", "nomeCoordenadorLider", "cnpjCoordenadorLider", "nomeTipoRequerimento", "nomeValorMobiliario", "statusDaOferta", "numeroProcesso", "numeroRegistro", "valorTotalEmReais", "possuiBook", "data")


def parse_brl_to_float(value: Any) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    if not isinstance(value, str) or not value.strip():
        return 0.0
    try:
        return float(value.replace("R$", "").replace(".", "").replace(",", ".").strip())
    except ValueError:
        return 0.0


def export_csv_offers(data: dict[str, Any], destination: Path | None = None) -> Path:
    records = data.get("registros", [])
    if not records:
        raise ValueError("Não há ofertas para exportar.")
    destination = destination or ROOT_DIR / "offers.xlsx"
    console_ok("Exportando ofertas...")
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Ofertas"
    sheet.append(HEADERS)
    header_fill = PatternFill("solid", fgColor="1F4E79")
    for current_cell in sheet[1]:
        current_cell.fill = header_fill
        current_cell.font = Font(bold=True, color="FFFFFF")
        current_cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    values: list[float] = []
    offers_with_book = 0
    for offer in records:
        amount = parse_brl_to_float(offer.get("valorTotalEmReais"))
        if amount > 0:
            values.append(amount)
        if str(offer.get("possuiBook", "")).casefold() in {"true", "sim", "s", "1"}:
            offers_with_book += 1
        offer_id = offer.get("idRequerimento")
        sheet.append([*(offer.get(field) for field in FIELDS), "Link Oferta" if offer_id else "N/A"])
        if offer_id:
            link = sheet.cell(sheet.max_row, 14)
            link.hyperlink = f"{OFFER_URL}{offer_id}"
            link.style = "Hyperlink"

    total = len(records)
    summaries = (("RESUMO ESTATÍSTICO", ""), ("Total de ofertas", total), ("Volume total (R$)", sum(values)), ("Ticket médio (R$)", sum(values) / len(values) if values else 0), ("Maior oferta (R$)", max(values, default=0)), ("Menor oferta (R$)", min(values, default=0)), ("Ofertas com bookbuilding", f"{offers_with_book} ({offers_with_book / total:.1%})"))
    sheet.append([])
    for label, value in summaries:
        sheet.append((label, value))
        sheet.cell(sheet.max_row, 1).font = Font(bold=True)
    for index, column in enumerate(sheet.iter_cols(), start=1):
        width = min(max(len(str(item.value or "")) for item in column) + 2, 60)
        sheet.column_dimensions[get_column_letter(index)].width = max(width, 10)
    sheet.freeze_panes = "A2"
    workbook.save(destination)
    console_ok(f"Arquivo salvo em: {destination}")
    return destination
