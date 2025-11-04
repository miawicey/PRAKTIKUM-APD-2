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
    table.field_names = ["Nama", "Elemen", "Rarity", "Senjata", "Region", "Role", "Skill"]
    for c in characters:
        table.add_row([c['nama'], c['elemen'], c['rarity'], c['senjata'], c['region'], c['role'], c['skill']])
    print(table)

def tampilkan_items():
    if not items:
        print("Belum ada item.")
        return
    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Kategori", "Rarity", "Efek", "Harga"]
    for i in items:
        table.add_row([i['id'], i['nama'], i['kategori'], i['rarity'], i['efek'], i['harga']])
    print(table)

def cari_character(nama):
    for c in characters:
        if c["nama"].lower() == nama.lower():
            return c
    return None

def cari_item(id_item):
    for i in items:
        if i["id"].lower() == id_item.lower():
            return i
    return None

def menu_admin():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        show_title("MENU PENGUASA GAME")

        pilih = list_input("Pilih menu", choices=[
            "Tambah Character",
            "Lihat Character",
            "Ubah Character",
            "Hapus Character",
            "Tambah Item",
            "Lihat Item",
            "Ubah Item",
            "Hapus Item",
            "Logout"
        ])

        if pilih == "Tambah Character":
            show_title("TAMBAH CHARACTER")
            nama = input("Nama: ")
            elemen = input("Elemen: ")
            rarity = input("Rarity: ")
            senjata = input("Senjata: ")
            region = input("Region: ")
            role = input("Role: ")
            skill = input("Ultimate Skill: ")
            characters.append({
                "nama": nama, "elemen": elemen, "rarity": rarity,
                "senjata": senjata, "region": region, "role": role, "skill": skill
            })
            print("Character berhasil ditambah.")

        elif pilih == "Lihat Character":
            show_title("DAFTAR CHARACTER")
            tampilkan_characters()

        elif pilih == "Ubah Character":
            nama = input("Nama character: ")
            c = cari_character(nama)
            if c:
                c["senjata"] = input("Senjata baru: ")
                print("Berhasil diubah.")
            else:
                print("Character tidak ditemukan.")

        elif pilih == "Hapus Character":
            nama = input("Nama character: ")
            c = cari_character(nama)
            if c:
                characters.remove(c)
                print("Character dihapus.")
            else:
                print("Tidak ditemukan.")

        elif pilih == "Tambah Item":
            id_item = input("ID Item: ")
            nama_item = input("Nama Item: ")
            kategori = input("Kategori: ")
            rarity = input("Rarity: ")
            efek = input("Efek: ")
            harga = input("Harga: ")
            items.append({
                "id": id_item, "nama": nama_item, "kategori": kategori,
                "rarity": rarity, "efek": efek, "harga": harga
            })
            print("Item berhasil ditambah.")

        elif pilih == "Lihat Item":
            show_title("DAFTAR ITEM")
            tampilkan_items()

        elif pilih == "Ubah Item":
            id_item = input("ID Item: ")
            i = cari_item(id_item)
            if i:
                i["efek"] = input("Efek baru: ")
                print("Berhasil diubah.")
            else:
                print("Item tidak ditemukan.")

        elif pilih == "Hapus Item":
            id_item = input("ID Item: ")
            i = cari_item(id_item)
            if i:
                items.remove(i)
                print("Item dihapus.")
            else:
                print("Tidak ditemukan.")

        elif pilih == "Logout":
            break

        input("Tekan Enter...")
