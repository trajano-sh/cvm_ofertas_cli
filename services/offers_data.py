import csv
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

CSV_FILE = Path("./data/oferta_resolucao_160.csv")

def load_offers() -> list[dict]:
    with CSV_FILE.open("r", encoding="latin-1", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        return list(reader)

def find_by_issuer(name: str) -> list[dict]:
    offers = load_offers()
    result = []
    for offer in offers:
        issuer = offer.get("Nome_Emissor") or ""
        if name.lower() in issuer.lower():
            result.append(offer)
    return result