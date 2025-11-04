def login(username, password):
    print(f"Memverifikasi {username}...")
    if username == "admin" and password == "123":
        return True
    return False



#SOAL 1
#  # import datetime

# sekarang = datetime.datetime.now()
# sekarang_formatted = sekarang.strftime("%d/%m/%Y, %H:%M:%S")
# print(sekarang_formatted)

# SOAL 2
# import random

# def generate_password():
#     characters = "abcdefghijklmnopqrstuv0123456789"
#     password_chars = random.choices(characters, k=12)
    
#     # Gabungkan menjadi string tunggal
#     password = ''.join(password_chars)
    
    return password

# # Contoh penggunaan
# kata_sandi_baru = generate_password()
# print("Kata sandi baru:", kata_sandi_baru)
