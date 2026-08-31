import os

def banner()->str:
    clear()
    with open("banner.txt","r",encoding="utf-8") as banner_:
        banner_ = banner_.read()
    return banner_

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')