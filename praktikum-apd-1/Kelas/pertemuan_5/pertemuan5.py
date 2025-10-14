# LIST AND TUPLE
# print("=== LIST AND TUPLE ===")
# my_list = [1, 2, 3, 4, 5]
# print("List:", my_list[2])
# my_tuple = (1, 2, 3, 4, 5)
# print("Tuple:", my_tuple[2])    
# print()

# matakuliah=['APD', 'KALKULUS', 'ORSIKOM', 'BASDAT', 'PBO']
# # for i in matakuliah:
# #     print(f'matakuliah{1}')
 
# for index, i in enumerate(matakuliah):
#     print(index)

    #enumarate itu untuk membaca index 


# matakuliah [0]
# print(matakuliah[0])
# print(matakuliah[2])
# print(matakuliah[-1])

# matakuliah.append('kalkulus')
# print(matakuliah)

# # fungsi append 
# matakuliah.append('bahasa inggris')
# print(matakuliah)

# matakuliah.insert(0, 'ipa')
# print(matakuliah)

# matakuliah.remove('ipa')
# print(matakuliah)

# NESTED LIST
# kelompok1 = ['ani', 'budi', 'cici']
# kelompok2 = ['dodi', 'erik', 'fifi']
# kelompok3 = ['gita', 'hadi', 'inti']
# kelas = [kelompok1, kelompok2, kelompok3]
# print(kelas)

# kelas.insert(2, ['joko', 'lina', 'mira'])
# print(kelas)

# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# print(studyclub)
# # Kita akan mengganti elemen di indeks ke-2, yakni "Multimedia"
# studyclub[2] = "AI"
# studyclub[1] = "APD"
# print(studyclub)
# # output awal
# ['Data Science', 'Robotics', 'Multimedia', 'Network']
# # output sesudah
# ['Data Science', 'Robotics', 'AI', 'Network']

# del studyclub[2]
# print(studyclub)

# # studyclub.remove("Network")
# # print(studyclub)

# studyclub.pop("network")
# print(studyclub)

# hapus = matakuliah.pop(2)
# print(studyclub)


# # OPERATOR LIST

# list = [1,2,3]
# # print(sum(list)/len(list))

# # print()

# nilai = [4,5,6,7,8,9]
# hasil = list+nilai 
# kali = list*nilai

# print("Lihat hasil penjumlahan:", hasil)
# print("Lihat hasil penjumlahan:", kali)

# Membuat Nested List
# kelas = [
# ["Ridho", "Lian", "Nabil"],
# ["Daffa", "Dante", "Santoso"],
# ["Pernanda", "Riyadi", "Ahnaf"],
# ]

# for i in kelas:
#     for b in i:
#          print(b)
# # kelas[2].insert(2, ['joko'])
# # print(kelas)

# # # # Memanggil elemen "Santoso"
# print(kelas[2][3])
# print(kelas[1])

# for i in kelas:
#     print(kelas)

# TUPLE
#mendefinisikan tuple
# anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
# print(anggota[1])
# print(anggota[-1])
# print(anggota[5][0])

# studyclub = ("Data Science", "Robotics", "Multimedia", "Network")
# liststudy=list(studyclub)

# liststudy[1] ="web"
# studyclub = ("Data Science", "Robotics", "Multimedia", "Network")

# liststudy=list(studyclub)
# # Tambahkan Web
# liststudy.append("Web")
# # ubah kembali list menjadi tuple
# tuplestudy=tuple(liststudy)
# print(tuplestudy)


# studi kasus
# List awal
keranjang = ["Brokoli", "Apel", "Jamur", "Nanas", "Wortel", "Kiwi", "Kol", "Sawi", "Lobak"]
buah = ["Apel", "Nanas", "Kiwi"]
# Menyaring hanya buah
buah_saja = [item for item in keranjang if item in buah]

# Menampilkan hasil
print("Buah-buahan dalam keranjang:", buah_saja)


for i in buah:
    print(i)
