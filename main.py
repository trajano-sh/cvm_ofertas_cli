from cli import menu,formatted
from api.endpoints import list_all_offers, get_offer


def main():
    menu.menu()
    i = int(input("$ "))
    while True:
        if i == 1:
            i3 = input("Inicio (01/01/2022): ")
            i4 = input("Final (01/01/2022): ")
            formatted.print_rich_table(list_all_offers(i3,i4))
            i2 = input("Abrir oferta: ")
            formatted.format_get_offer(get_offer(i2),i2)
            break
        else:
            print("invalid")
            

if __name__ == "__main__":
    main()