# PERULANGAN FOR
# for i in range (10):
#     print(i)

# for i in range(1,11,2):
#     print(i)
#     # i adalah variabel nya dri data tsb 

# pengulangan pada suatu kata 

# While
# jawaban ="yaa"
# while (jawaban =="yaa") :
#     jawab= input("apakah kamu mau mengulang? (yaa/tidak)")
#     print(f"jawaban kamu adalah {jawaban}")

# while (jawab=="yaa"):
#     hitung +=1
#     jawab= input("ulang lagi?:")
#     print(f"jawaban kamu adalah {jawab}")

# cuaca = "Hujan"
# while ( cuaca == "Hujan" or "hujan"):
#     print("woi keluar rumah kamu mati kedinginan")
#     cuaca = input("Bagaimana cuaca hari ini?")

# print("Kamu selamat dari kematian")

# angka = 10
# while (angka>1):
#     print(angka)
#     angka -=3

#NESTED LOOP
# for  i in range(1,6):
#     for j in range(1,6):
#         print(f"i = {i} x {j}={i*j}")
#         print("")

# control pengulangan
# angka = [4,5,6,7,10,11,15,17,19]
# print(f"mencari angka yang lebih besar dari 10")
 
# for i in angka:
#     print(f"memeriksa angka{i}")
#     if i > 10:
#     print(f'{i} lebih besar dari 10')
#       break
# print("Programnnyaaa selesai")


# for i in range(1,20):
#     if i%2 ==0:
#         continue
#     print(f'Angka genap ditemukan :{i}')
    
# print("Program selesai")

# for i in range(1, 20):
#     if i % 2 != 0:   # skip ganjil
#         continue
#     print(f'Angka genap ditemukan : {i}')

# print("Program selesai")


  # HELLO KITY HANCURRRR
# rows = 20
# cols = 40

# # for i in range(rows):
#     for j in range(cols):
#         # pita kiri
#         if (i in range(2,5) and j in range(10,14)):
#             print("@", end="")
#         # pita kanan
#         elif (i in range(2,5) and j in range(26,30)):
#             print("@", end="")
#         # telinga kiri
#         elif (i < 5 and j == 5) or (i == 4 and j in range(5,10)):
#             print("*", end="")
#         # telinga kanan
#         elif (i < 5 and j == 30) or (i == 4 and j in range(30,35)):
#             print("*", end="")
#         # kepala
#         elif (i >= 5 and i < 15 and j > 5 and j < 35):
#             print("*", end="")
#         # mata
#         elif (i == 9 and j in [12, 27]):
#             print("O", end="")
#         # hidung
#         elif (i == 11 and j == 20):
#             print("^", end="")
#         # kumis kiri
#         elif (i == 10 and j in [8, 9]):
#             print("-", end="")
#         elif (i == 11 and j in [7, 8]):
#             print("-", end="")
#         # kumis kanan
#         elif (i == 10 and j in [31, 32]):
#             print("-", end="")
#         elif (i == 11 and j in [32, 33]):
#             print("-", end="")
#         else:
#             print(" ", end="")
#     print()

# angka_genap = [x for x in range(1, 21) if x % 2 == 0]

# for x in range(1,21):
#     if x % 2 == 0:
#         print(f"angka genap ditemukan: {x}")
# print("Program selesai")

# angka_ganjil = [x for x in range =(1,21) if x % 2 !=0]
# for x in range (1,21):
#     if x % 2 !=0:
#         print(f"angka ganjil ditemukan: {x}")       

# Minta input tinggi segitiga
# n = int(input("Masukkan tinggi segitiga: "))

# print("\nSegitiga Sama Kaki:")
# for i in range(1, n+1):  
#     for j in range(n-i):
#         print(" ", end="")
#     for k in range(2*i-1):
#         print("*", end="")
#     print()

# print("\nSegitiga Sama Kaki Terbalik:")
# for i in range(n, 0, -1):  
#     for j in range(n-i):
#         print(" ", end="")
#     for k in range(2*i-1):
#         print("*", end="")
#     print()

# print("\nSegitiga siku siku:")
# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end="")
#     print()

print("segitiga sikun siku :")
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()

print("\n segitiga siku siku terbalik kanan:")
for i in range(6,1):
    for j in range(i):
        print("*", end="")

for i in range(1,6):
    for j in range(5-i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

for i in range(1,6):
    for j in range(i-5):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

print("\n bulat:")
for i in range(7):
    for j in range(7):
        if (i == 0 and j in [2,3,4]) or (i == 1 and j in [1,5]) or (i == 2 and j in [0,6]) or (i == 3 and j in [0,6]) or (i == 4 and j in [0,6]) or (i == 5 and j in [1,5]) or (i == 6 and j in [2,3,4]):
            print("*", end="")
        else:
            print(" ", end="")
    print()



