from __future__ import annotations

import requests
from zipfile import BadZipFile

from api.endpoints import CVMApiError, get_offer, list_all_offers
from cli.formatted import format_get_offer, print_offers_table, print_rich_table
from cli.menu import show_menu
from config.config import CSV_FILE
from export.excel import export_csv_offers
from scripts.fetch_data import ensure_data_file
from services.offers_data import find_by_issuer
from utils.utils import clear, console_error, console_warn

YES = {"s", "sim"}


def _open_offer(offer_id: str) -> None:
    if offer_id.strip():
        format_get_offer(get_offer(offer_id), offer_id)
        input("Pressione Enter para continuar...")


def _filter_by_period() -> None:
    date_start = input("Início (DD/MM/AAAA, vazio = últimos 30 dias): ").strip()
    date_end = input("Final (DD/MM/AAAA, vazio = hoje): ").strip()
    data = list_all_offers(date_start, date_end)
    if not print_rich_table(data, date_start, date_end):
        return
    if input("Deseja exportar o arquivo? (S/N): ").strip().casefold() in YES:
        export_csv_offers(data)
    _open_offer(input("Digite um ID para abrir ou Enter para voltar: "))


def _detailed_search() -> None:
    console_warn("Valores atualizados até o último dia útil.")
    try:
        ensure_data_file()
    except (requests.RequestException, OSError, BadZipFile) as error:
        if not CSV_FILE.is_file():
            raise
        console_warn(f"Não foi possível atualizar a base; usando o arquivo local. Motivo: {error}")
    query = input("Digite o que deseja procurar: ")
    print_offers_table(find_by_issuer(query))


def main() -> None:
    actions = {
        "1": _filter_by_period,
        "2": lambda: _open_offer(input("ID da oferta: ")),
        "3": _detailed_search,
    }
    while True:
        show_menu()
        choice = input("Escolha uma opção: ").strip()
        if choice == "0":
            print("Até logo!")
            return
        action = actions.get(choice)
        if action is None:
            clear()
            console_warn("Opção inválida.")
            continue
        try:
            action()
        except (CVMApiError, ValueError, OSError, BadZipFile, requests.RequestException) as error:
            console_error(str(error))


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nOperação cancelada.")
