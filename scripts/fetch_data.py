from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from shutil import copyfileobj
from zipfile import BadZipFile, ZipFile

import requests

from config.config import CSV_FILE, ZIP_FILENAME, ZIP_URL
from utils.utils import console_ok

DATA_DIR = CSV_FILE.parent
DOWNLOAD_TIMEOUT = (5, 120)


def _is_current(path: Path) -> bool:
    return path.is_file() and path.stat().st_size > 0 and datetime.fromtimestamp(path.stat().st_mtime).date() == date.today()


def download_file(url: str, filename: str) -> Path:
    console_ok("Baixando base de dados...")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    destination = DATA_DIR / filename
    temporary = destination.with_suffix(f"{destination.suffix}.part")
    try:
        with requests.get(url, stream=True, timeout=DOWNLOAD_TIMEOUT) as response:
            response.raise_for_status()
            with temporary.open("wb") as output:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        output.write(chunk)
        temporary.replace(destination)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return destination


def extract_zip_file(zip_path: Path, filename: str) -> Path:
    console_ok("Extraindo base de dados...")
    destination = DATA_DIR / Path(filename).name
    temporary = destination.with_suffix(f"{destination.suffix}.part")
    try:
        with ZipFile(zip_path) as archive:
            if filename not in archive.namelist():
                available = ", ".join(archive.namelist())
                raise FileNotFoundError(f"{filename!r} não existe em {zip_path.name}. Arquivos: {available}")
            with archive.open(filename) as source, temporary.open("wb") as output:
                copyfileobj(source, output, length=1024 * 1024)
        temporary.replace(destination)
    except (BadZipFile, OSError):
        temporary.unlink(missing_ok=True)
        raise
    return destination


def ensure_data_file(force: bool = False) -> Path:
    if not force and _is_current(CSV_FILE):
        return CSV_FILE
    zip_path = download_file(ZIP_URL, ZIP_FILENAME)
    return extract_zip_file(zip_path, CSV_FILE.name)


def extract_zip() -> Path:
    return ensure_data_file()
