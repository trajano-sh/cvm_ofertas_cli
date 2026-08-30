from datetime import datetime, date,timedelta
import json
import requests
from typing import Dict, Any, Union, Optional

URL_BASE = "https://web.cvm.gov.br/sre-publico-cvm/rest/sitePublico/pesquisar"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Content-Type": "application/json;charset=UTF-8",
    "Accept": "application/json, text/plain, */*"
}

def payload_json(
        date_start: Optional[Union[datetime,date,str]] =None,
        date_end: Optional[Union[datetime,date,str]] = None,
        page:int = 1,
        size_page:int = 10) -> Dict[str,Any]:
    today = date.today()
    if date_start is None:
        date_start = today

    if date_end is None:
        date_end = today - timedelta(days=30)

    dt_start = date_start.strftime("%d/%m/%Y") if isinstance(date_start, (datetime, date)) else date_start
    dt_end = date_end.strftime("%d/%m/%Y") if isinstance(date_end, (datetime, date)) else date_end
    payload = {
        "periodoCriacaoProcesso":{
            "de":dt_start,
            "ate":dt_end
            },
        "opa":False,
        "tipoOferta":"OFERTA_REGULAR",
        "modalidade":"TODAS",
        "direcaoOrdenacao":"DESC",
        "colunaOrdenacao":"data",
        "pagina":page,
        "tamanhoPagina": size_page
    }
    return payload

def list_all_offers(
    date_start: Optional[Union[datetime, date, str]] = None, 
    date_end: Optional[Union[datetime, date, str]] = None, 
    page: int = 1, 
    size_page: int = 10
) -> Dict[str, Any]:
    url = f"{URL_BASE}/detalhado"
    body = payload_json(date_start=date_start, date_end=date_end, page=page, size_page=size_page)
    
    response = requests.post(url=url, json=body, headers=HEADERS, timeout=30)
    response.raise_for_status()
    return response.json()

def get_offer(offer_id: int):
    response = requests.get(url=f"{URL_BASE}/informacoesGerais/{offer_id}")
    date = response.json()
    return date