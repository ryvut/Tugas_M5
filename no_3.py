warna = ("Merah", "Kuning", "Hijau")

try:
    warna[0] = "Biru"
except TypeError as e:
    print("Pesan error yang muncul:", e)