import os
os.system("cls" if os.name == "nt" else "clear")
print("=================================")
print("       SISTEM RENTAL MOBIL        ")
print("=================================")

# Autentikasi
username1 = "vita"   
password1 = "041"    
percobaan = 0
makspercobaan = 5

while percobaan < makspercobaan:
    username = input("Masukkan Username: ")
    password = input("Masukkan Password (3 digit terakhir NIM): ")

    if username == username1 and password == password1:
        print("\nLogin nya berhasil, goodjob! Selamat datang, {username1}!")
        break
    else:
        percobaan += 1
        print("Username atau password salah!\n")
        if percobaan == makspercobaan:
            print("hai kamu banyak mencoba juga ya, silahkan coba lagi.")
            exit()

tarif_standar = 500000
tarif_premium = 1200000

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=================================")
    print("           MENU UTAMA             ")
    print("=================================")
    print("1. Input Data Customer")
    print("2. Keluar dari Program")
    print("=================================")
    pilihan = input("Pilih menu (1/2): ")

    if pilihan == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("=================================")
        print("       INPUT DATA CUSTOMER       ")
        print("=================================")

        # Input data customer
        nama = input("Masukkan nama customer: ")
        usia = int(input("Masukkan usia customer: "))
        punya_sim = input("Apakah memiliki SIM A? (ya/tidak): ")
        deposit = int(input("Masukkan jumlah deposit (Rp): "))
        pengalaman = int(input("Masukkan lama pengalaman mengemudi (tahun): "))

        print("\nHasil Pengecekan:")
        print("------------------")

        if usia < 21:
            print("Tolak: Usia tidak mencukupi")
        elif punya_sim != "ya":
            print("Tolak: Tidak memiliki SIM A")
        elif deposit < 500000:
            print("Tolak: Deposit tidak mencukupi")
        elif pengalaman < 1:
            print("Tolak: Pengalaman mengemudi kurang dari 1 tahun")
        else:
            print("Data diterima. Lanjut ke pemilihan mobil.")

            mobil = None
            harga = 0
            print("\nPilihan Mobil:")
            print("1. Mobil Standar")
            print("2. Mobil Premium")
            pilihan_mobil = input("Pilih jenis mobil (1/2): ")

            if pilihan_mobil == "1":
                mobil = "Mobil Standar"
                harga = tarif_standar
            elif pilihan_mobil == "2":
                if pengalaman < 4:
                    print("Tolak: Pengalaman kurang untuk mobil premium")
                else:
                    mobil = "Mobil Premium"
                    harga = tarif_premium
            else:
                print("Pilihan tidak bagus, silahkan coba lagi!!")
                

            if mobil:
                lama_sewa = int(input(f"Berapa hari ingin menyewa {mobil}? "))
                total_bayar = harga * lama_sewa
                print("\n=================================")
                print("\n")
                print("          STRUK SEWA SEWA MOBIL       ")
                print("=================================")
                print(f"Nama Customer   : {nama}")
                print(f"Mobil Dipilih   : {mobil}")
                print(f"Lama Sewa       : {lama_sewa} hari")
                print(f"Total Bayar     : Rp{total_bayar:,}")
                print("=================================")
                input("\nTekan ENTER untuk kembali ke menu...")

    elif pilihan == "2":
        print("\nTerima kasih telah menggunakan layanan rental mobil!")
        break
    else:
        print("\nPilihan tidak baik, silahkan coba lagi!!")
        input("Tekan ENTER untuk lanjut...")
