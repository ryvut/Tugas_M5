kendaraan = ("Motor", "Mobil", "Sepeda")

list_kendaraan = list(kendaraan)

list_kendaraan[1] = "Bus"

kendaraan_baru = tuple(list_kendaraan)

print("Hasil akhir tuple kendaraan:", kendaraan_baru)
print("Tipe data akhir:", type(kendaraan_baru))