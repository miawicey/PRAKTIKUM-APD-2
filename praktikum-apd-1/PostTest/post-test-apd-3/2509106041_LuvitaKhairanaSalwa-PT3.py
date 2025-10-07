print("=================================") 
print(" SISTEM RENTAL MOBIL") 
print("=================================")

# INPUT DATA CUSTOMER
nama = input("Masukkan nama customer: ")
usia = int(input("Masukkan usia customer: "))
punya_sim = input("Apakah memiliki SIM A? (ya/tidak): ") 
deposit = int(input("Masukkan jumlah deposit (harus diatas 500.000 ) (Rp): "))
pengalaman = int(input("Masukkan lama pengalaman mengemudi (tahun): "))
print("=================================")

print("Hasil Pengecekan:")
print("------------------") 


# Proses pengecekan syarat 
if usia < 21: print("Tolak: Usia tidak mencukupi")
elif punya_sim != "ya": print("Tolak: Tidak memiliki SIM A") 
elif deposit < 500.000: print("Tolak: Deposit tidak cukup") 
elif pengalaman < 4: print("Setujui untuk mobil standar saja")
else:
     print("Setujui untuk semua jenis mobil")


print("=================================")
print("Terima kasih telah menggunakan layanan kami!")
print("Kenyamanan anda adalah prioritas kami")
print("===================================")
