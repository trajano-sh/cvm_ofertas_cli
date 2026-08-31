from pathlib import Path
from zipfile import ZipFile

import requests

from config.config import ZIP_URL, ZIP_FILENAME, ROOT_DIR
from utils.utils import console_ok

URL = ZIP_URL

DATA_DIR = ROOT_DIR / "database"
DATA_DIR.mkdir(exist_ok=True)


def download_file(url: str, filename: str) -> Path:
    console_ok("Downloading file...")
    destination = DATA_DIR / filename
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    destination.write_bytes(response.content)
    return destination


def extract_zip_file(zip_path: Path, filename: str) -> Path:
    console_ok("Extracting file...")
    with ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extract(filename, DATA_DIR)
    return DATA_DIR / filename


if __name__ == "__main__":
    zip_path: Path = download_file(url=URL, filename=ZIP_FILENAME)
    csv_path = extract_zip_file(zip_path=zip_path, filename=ZIP_FILENAME)
    print(f"Save in: {csv_path}")
