
# buah = ([“apel”, “jeruk”, “mangga”, “apel”])
# for i in buah
#     print=(i

# angka= [1,2,3,4,5,6,7,8]
# unik= int(angka)
# print(unik)


# # Daftar_buku = {
# # "Buku1" : "Bumi Manusia",
# # "Buku2" : "Laut Bercerita"
# # }

# # print(Daftar_buku["Buku1"])

# # print(Daftar_buku)

# print(daftar buku{buku1})


# Biodata = {
# "Nama" : "Ananda Daffa Harahap",
# "NIM" : 2409106050,
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Social Media" : {"Instagram" : "daffahrhap"}
# }

# for i, j in Biodata.items():
#     print(i)
#     print(j)

    # gunanya buat mengambil hal hal di key dan value secara bersamaan
# Biodata = { 
#     "Nama" : "Ananda Daffa Harahap", 
#     "NIM" : 2409106050, 
#     "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"], 
#     "Mahasiswa_Aktif" : True, 
#     "Social Media" : {"Instagram" : "daffahrhap"} 
# }

# print(f"nama saya adalah {Biodata['Nama']}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get('Nama')}")
# print(Biodata.get('Nama'))

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror", }

# print(Film)
# Filnm.clear

# hapus = Film.pop ("The Conjuring")
# print (film)

# Film["Zombieland"] = "Comedy"
# Film.update({"upin ipin" : "Thriller"})
# #Setelah Ditambah
# print(Film)

# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", 
#                 ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# }

# print(Musik['Paramore'][2][0][1])

# angka= set()
# print{type(angka)}

# a = {10,11,12}
# b={11,12,14}
# c= a/b
# print(c)

# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
# print(f"Musik milik {i} adalah : ")
# for song in j:
# print(song)
# print("")

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# print("Nilai : ", Nilai.setdefault("Kimia",   90))
# print("")

mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]]

# perulangan for untuk mendapatkan semua elemen
for i in mahasiswa:
    for j in i:
        print(j)
