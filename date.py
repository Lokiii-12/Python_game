import datetime as dt

print("Masukan tanggal lahir, bulan, dan tahun Anda:")
tanggal = int(input("Masukan Tanggal Lahir Anda\t: "))
bulan = int(input("Masukan Bulan Lahir Anda\t: "))
tahun = int(input("Masukan Tahun Lahir Anda\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
hari_ini = dt.date.today()
umur = hari_ini.year - tanggal_lahir.year - ((hari_ini.month, hari_ini.day) < (tanggal_lahir.month, tanggal_lahir.day))
print(f"Umur Anda adalah {umur} tahun")
jam = dt.datetime.now().hour
if 0 <= jam < 10:
    print("Selamat pagi!")
elif 10 <= jam < 15:
    print("Selamat siang!")
elif 15 <= jam < 18:
    print("Selamat sore!")
else:
    print("Selamat malam!")
print("Terima kasih telah menggunakan program ini.")
"""
Ya singkatnya gini si
"""