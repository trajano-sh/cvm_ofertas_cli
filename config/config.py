import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = ROOT_DIR / "config" / "settings.json"


def load_config() -> dict:
    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


CONFIG = load_config()

BANNER_PATH = ROOT_DIR / CONFIG["paths"]["banner"]
CSV_FILE = ROOT_DIR / CONFIG["paths"]["csv_file"]

API_BASE_URL = CONFIG["api"]["base_url"]
DETAILED_ENDPOINT = CONFIG["api"]["detailed_endpoint"]
GENERAL_INFO_ENDPOINT = CONFIG["api"]["general_info_endpoint"]
OFFER_URL = CONFIG["api"]["offer_url"]

ZIP_URL = CONFIG["data_source"]["zip_url"]
ZIP_FILENAME = CONFIG["data_source"]["zip_filename"]

DEFAULT_PAGE_SIZE = CONFIG["defaults"]["page_size"]
