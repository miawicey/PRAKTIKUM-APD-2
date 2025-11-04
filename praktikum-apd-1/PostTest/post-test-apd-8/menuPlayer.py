import os
from prettytable import PrettyTable
from data import characters, items
from inquirer import list_input

def show_title(teks):
    print("═" * 60)
    print(f"║ {teks.center(56)} ║")
    print("═" * 60)

def tampilkan_characters():
    if not characters:
        print("Belum ada character.")
        return
    table = PrettyTable()
    table.field_names = ["Nama", "Elemen", "Rarity", "Senjata"]
    for c in characters:
        table.add_row([c['nama'], c['elemen'], c['rarity'], c['senjata']])
    print(table)

def tampilkan_items():
    if not items:
        print("Belum ada item.")
        return
    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Kategori", "Harga"]
    for i in items:
        table.add_row([i['id'], i['nama'], i['kategori'], i['harga']])
    print(table)

def menu_player():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        show_title("MENU PLAYER")

        pilih = list_input("Pilih menu", choices=[
            "Lihat Character",
            "Lihat Item",
            "Logout"
        ])

        if pilih == "Lihat Character":
            show_title("CHARACTER TERSEDIA")
            tampilkan_characters()
        elif pilih == "Lihat Item":
            show_title("ITEM TERSEDIA")
            tampilkan_items()
        elif pilih == "Logout":
            break

        input("Tekan Enter...")
