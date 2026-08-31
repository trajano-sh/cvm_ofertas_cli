from InquirerPy import inquirer
from export.csv_export import export_csv_offers
from api.endpoints import list_all_offers, get_offer
from cli import formatted
from export.csv_export import export_csv_offers


def main():
    while True:
        options = ["Procurar por periodo", "Abrir por id", "exit"]
        choice = inquirer.select(message="Selecione um option", choices=options, default=options[0]).execute()

        if choice == options[2]:
            print("Goodbye")
            break
        elif choice == options[0]:
            i3 = input("Inicio: ")
            i4 = input("Final: ")
            date = list_all_offers(i3,i4)
            formatted.print_rich_table(date)
            export_csv_offers(date)
            if not date:
                continue
            i2 = input("Abrir oferta: ")
            formatted.format_get_offer(get_offer(i2), i2)
            break
        elif choice == options[1]:
            i2 = input("Abrir oferta: ")
            formatted.format_get_offer(get_offer(i2), i2)


if __name__ == "__main__":
    main()
