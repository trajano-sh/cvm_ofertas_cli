from pygments import formatter

from cli.menu import show_menu
from export.excel import export_csv_offers
from api.endpoints import list_all_offers, get_offer
from cli.formatted import print_offers_table,print_rich_table,format_get_offer
from export.excel import export_csv_offers
from services.offers_data import find_by_issuer
from utils.utils import clear, console_warn


def main():
    while True:
        show_menu()
        choice = str(input("Escolha uma opção: "))
        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            i3 = input("Inicio: ")
            i4 = input("Final: ")
            date = list_all_offers(i3, i4)
            print_rich_table(date,i3,i4)
            i1 = input("Deseja exportar o arquivo? (S/N): ")

            if i1.lower() == "s" or i1.lower() == "sim".lower():
                export_csv_offers(date)

            elif i1.lower() == "n" or i1.lower() == "nao".lower():
                pass
            i2 = input("Digite um id para abrir: ")
            if i2.strip() == "":
                continue
            format_get_offer(get_offer(i2),i2)

        elif choice == "2":
            i2 = str(input("Abrir oferta: "))
            format_get_offer(get_offer(i2),i2)

        elif choice == "3":
            console_warn("\nValores atualizados até o último dia útil\n")

            search = input("Digite oque deseja procurar: ")
            print_offers_table(find_by_issuer(search))
            break
        else:
            clear()
            print("Option invalid")

if __name__ == "__main__":
    main()