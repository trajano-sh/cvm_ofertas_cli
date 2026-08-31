import csv
import sys
from config.config import CSV_FILE, ROOT_DIR
from utils.utils import console_ok

sys.path.insert(0, str(ROOT_DIR))


def load_offers() -> list[dict]:
    with CSV_FILE.open("r", encoding="latin-1", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        return list(reader)


def find_by_issuer(query: str) -> list[dict]:
    console_ok(f"Searching offers for: {query}")
    offers = load_offers()
    result = []

    target_columns = ["Nome_Emissor", "Numero_Requerimento", "Numero_Processo", "CNPJ_Emissor","CNPJ_Lider","Nome_Lider","Destinacao_recursos","Ativos_alvo","Administrador","Gestor","Agente_fiduciario","Escriturador",""]
    query_lower = query.lower()

    for offer in offers:
        for col in target_columns:
            val = offer.get(col)
            if val and query_lower in str(val).lower():
                result.append(offer)
                break

    return result