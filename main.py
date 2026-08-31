from InquirerPy import inquirer

from cli.menu import show_menu
from export.excel import export_csv_offers
from api.endpoints import list_all_offers, get_offer
from cli import formatted
from export.excel import export_csv_offers


def main():
    while True:
        show_menu()
        choice = int(input("Escolha uma opção: "))
        if choice == 0:
            print("Goodbye!")
            break
        elif choice == 1:
            i3 = input("Inicio: ")
            i4 = input("Final: ")
            date = list_all_offers(i3,i4)
            formatted.print_rich_table(date)
            i1 = input("Deseja exportar o arquivo? (S/N): ")
            if i1.lower() == "s" or i1.lower() == "sim".lower():
                export_csv_offers(date)
            elif i1.lower() == "n" or i1.lower() == "nao".lower():
                break
            break
        elif choice == 2:
            i2 = input("Abrir oferta: ")
            formatted.format_get_offer(get_offer(i2), i2)

if __name__ == "__main__":
    main()
