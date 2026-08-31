from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import Any

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config.config import API_BASE_URL, DEFAULT_PAGE_SIZE, DETAILED_ENDPOINT, GENERAL_INFO_ENDPOINT
from utils.utils import console_ok

DateInput = datetime | date | str | None
REQUEST_TIMEOUT = (5, 30)
HEADERS = {"User-Agent": "cvm-offers-cli/1.0", "Accept": "application/json"}


class CVMApiError(RuntimeError):
    pass


def _build_session() -> requests.Session:
    retry = Retry(total=3, backoff_factor=0.5, status_forcelist=(429, 500, 502, 503, 504), allowed_methods=frozenset({"GET", "POST"}))
    session = requests.Session()
    session.headers.update(HEADERS)
    session.mount("https://", HTTPAdapter(max_retries=retry))
    return session


SESSION = _build_session()


def _format_date(value: DateInput, default: date) -> str:
    if value is None or value == "":
        return default.strftime("%d/%m/%Y")
    if isinstance(value, (datetime, date)):
        return value.strftime("%d/%m/%Y")
    try:
        return datetime.strptime(value.strip(), "%d/%m/%Y").strftime("%d/%m/%Y")
    except ValueError as error:
        raise ValueError(f"Data inválida: {value!r}. Use DD/MM/AAAA.") from error


def payload_json(date_start: DateInput = None, date_end: DateInput = None, page: int = 1, size_page: int = DEFAULT_PAGE_SIZE) -> dict[str, Any]:
    if page < 1 or size_page < 1:
        raise ValueError("Página e tamanho da página devem ser maiores que zero.")
    today = date.today()
    start = _format_date(date_start, today - timedelta(days=30))
    end = _format_date(date_end, today)
    if datetime.strptime(start, "%d/%m/%Y") > datetime.strptime(end, "%d/%m/%Y"):
        raise ValueError("A data inicial não pode ser posterior à data final.")
    return {
        "periodoCriacaoProcesso": {"de": start, "ate": end},
        "opa": False, "tipoOferta": "OFERTA_REGULAR", "modalidade": "TODAS",
        "direcaoOrdenacao": "DESC", "colunaOrdenacao": "data",
        "pagina": page, "tamanhoPagina": size_page,
    }


def _request_json(method: str, endpoint: str, **kwargs: Any) -> dict[str, Any]:
    try:
        response = SESSION.request(method, f"{API_BASE_URL}{endpoint}", timeout=REQUEST_TIMEOUT, **kwargs)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as error:
        raise CVMApiError(f"Falha ao consultar a CVM: {error}") from error
    except ValueError as error:
        raise CVMApiError("A CVM retornou uma resposta JSON inválida.") from error
    if not isinstance(data, dict):
        raise CVMApiError("A CVM retornou uma resposta em formato inesperado.")
    return data


def list_all_offers(date_start: DateInput = None, date_end: DateInput = None, page: int = 1, size_page: int = DEFAULT_PAGE_SIZE) -> dict[str, Any]:
    console_ok("Consultando ofertas...")
    return _request_json("POST", DETAILED_ENDPOINT, json=payload_json(date_start, date_end, page, size_page))


def get_offer(offer_id: str | int) -> dict[str, Any]:
    normalized_id = str(offer_id).strip()
    if not normalized_id:
        raise ValueError("Informe um ID de oferta.")
    return _request_json("GET", f"{GENERAL_INFO_ENDPOINT}/{normalized_id}")
