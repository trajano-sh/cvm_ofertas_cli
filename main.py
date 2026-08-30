from cli import menu,formatted
from api.endpoints import list_all_offers, get_offer


def main():
    menu.menu()
    i = int(input("$ "))
    while True:
        if i == 1:
            formatted.format_offers_table(list_all_offers("01/01/2025","02/01/2025"))
            i2 = input("Abrir oferta: ")
            formatted.format_get_offer(get_offer(i2),i2)
            break
        else:
            print("invalid")
            

if __name__ == "__main__":
    main()