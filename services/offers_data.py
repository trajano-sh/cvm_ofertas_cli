import csv
import sys
from config.config import CSV_FILE, ROOT_DIR
from utils.utils import console_ok

sys.path.insert(0, str(ROOT_DIR))


def load_offers() -> list[dict]:
    with CSV_FILE.open("r", encoding="latin-1", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        return list(reader)


def find_by_issuer(name: str) -> list[dict]:
    console_ok("Finding offers by issuer")
    offers = load_offers()
    result = []
    for offer in offers:
        issuer = offer.get("Nome_Emissor") or ""
        if name.lower() in issuer.lower():
            result.append(offer)
    return result
