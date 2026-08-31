from __future__ import annotations

import csv
from collections.abc import Iterator

from config.config import CSV_FILE
from utils.utils import console_ok

SEARCH_COLUMNS = (
    "Nome_Emissor", "Numero_Requerimento", "Numero_Processo", "CNPJ_Emissor",
    "CNPJ_Lider", "Nome_Lider", "Destinacao_recursos", "Ativos_alvo",
    "Administrador", "Gestor", "Agente_fiduciario", "Escriturador",
)


def iter_offers() -> Iterator[dict[str, str]]:
    with CSV_FILE.open("r", encoding="latin-1", newline="") as file:
        yield from csv.DictReader(file, delimiter=";")


def load_offers() -> list[dict[str, str]]:
    return list(iter_offers())


def find_by_issuer(query: str) -> list[dict[str, str]]:
    normalized_query = query.strip().casefold()
    if not normalized_query:
        return []
    console_ok(f"Buscando ofertas por: {query.strip()}")
    return [offer for offer in iter_offers() if any(normalized_query in (offer.get(column) or "").casefold() for column in SEARCH_COLUMNS)]
