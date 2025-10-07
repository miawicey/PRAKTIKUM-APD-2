print("===== Supermarket Kasir Vita =====")
print("brum brum brum")
print("Welcome to my supermarket")
print()

# JENIS BARANG
barang1 = "Susu"
barang2 = "Nabati"
barang3 = "Indomie"

# HARGA BARANG
harga1 = 4000
harga2 = 3500
harga3 = 4000

# JUMLAH BARANG
jumlah1 = 30
jumlah2 = 20
jumlah3 = 10

# DISKON
diskon = 0.5   # 50%
#  APAKAH ADA DISKON?
ada_diskon = True   # kalau False, diskon otomatis 0

# PERTAMA KALI BELANJA LALU DIHITUNG
total1 = harga1 * jumlah1
total2 = harga2 * jumlah2
total3 = harga3 * jumlah3
subtotal = total1 + total2 + total3
potongan = subtotal * diskon * ada_diskon
total_bayar = subtotal - potongan

# CETAK STRUK
print("Barang:", barang1, "| Harga:", harga1, "| Jumlah:", jumlah1, "| Total:", total1)
print("Barang:", barang2, "| Harga:", harga2, "| Jumlah:", jumlah2, "| Total:", total2)
print("Barang:", barang3, "| Harga:", harga3, "| Jumlah:", jumlah3, "| Total:", total3)
print("-----------------------------------")
print("Subtotal:", subtotal)
print("Diskon 50%, potongan:", potongan)
print("Total Bayar:", total_bayar)
print("Ada Diskon?", ada_diskon)
print()
print("Terima Kasih")
print("Datang lagi yaaa ke supermarket Vita")
print("brum brum brum")
