from config.config import BANNER_PATH


def show_menu() -> None:
    print(BANNER_PATH.read_text(encoding="utf-8"))
    print("1) Filtrar por período\n2) Abrir por ID\n3) Pesquisa detalhada\n0) Sair\n")
