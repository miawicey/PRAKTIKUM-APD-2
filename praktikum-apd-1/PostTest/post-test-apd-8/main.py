import os
from inquirer import list_input
from data import users, login_login
from menuAdmin import menu_admin
from menuPlayer import menu_player

def show_title(teks):
    print("═" * 60)
    print(f"║ {teks.center(56)} ║")
    print("═" * 60)

def login(attempt=1):
    if attempt > login_login:
        print("Terlalu banyak gagal login. Program keluar.")
        exit()
    uname = input("Username: ")
    pw = input("Password: ")
    for u in users:
        if u["username"] == uname and u["password"] == pw:
            print(f"Login sukses! Selamat datang {uname.title()}")
            return u
    print("Login salah! Coba lagi.")
    return login(attempt + 1)

while True:
    os.system("cls" if os.name == "nt" else "clear")
    show_title("SISTEM GENSHIN IMPACT")

    pilih = list_input("Pilih menu", choices=["Login", "Register", "Keluar"])
    if pilih == "Login":
        user_login = login()
        if user_login["role"] == "penguasa":
            menu_admin()
        else:
            menu_player()

    elif pilih == "Register":
        uname = input("Username baru: ")
        if any(u["username"] == uname for u in users):
            print("Username sudah digunakan!")
        else:
            pw = input("Password: ")
            users.append({"username": uname, "password": pw, "role": "player"})
            print("Akun berhasil dibuat!")
        input("Tekan Enter...")

    elif pilih == "Keluar":
        print("Program selesai! Terima kasih bermain.")
        break
