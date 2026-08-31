from pathlib import Path
from zipfile import ZipFile
import requests

URL = "https://dados.cvm.gov.br/dados/OFERTA/DISTRIB/DADOS/oferta_distribuicao.zip"

DATA_DIR = Path("../data")
DATA_DIR.mkdir(exist_ok=True)

def download_file(url: str, filename: str) -> Path:
    destination = DATA_DIR / filename
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    destination.write_bytes(response.content)
    return destination

def extract_zip_file(zip_path: Path, filename: str) -> Path:
    with ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extract(filename, DATA_DIR)
    return DATA_DIR / filename

if __name__ == "__main__":
    zip_path: Path = download_file(url=URL,filename="oferta_distribuicao.zip")
    csv_path = extract_zip_file(zip_path=zip_path,filename="oferta_resolucao_160.csv")
    print(f"Archives save in: {csv_path}")