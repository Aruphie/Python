# Date and Time (Latihan)

import datetime as dt

print(("kalkulator umur".center(50,"-")).upper())
print("Silahkan masukan tanggal lahir : ")
Tanggal = int(input("Tanggal \t: "))
Bulan = int(input("Bulan \t\t: "))
Tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(Tahun,Bulan,Tanggal)
print(f"Tanggal lahir \t: {tanggal_lahir:%A}, {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini \t: {hari_ini:%A}, {hari_ini}")

umur = hari_ini - tanggal_lahir
print(f"Umur \t\t: {int(umur.days)//365} Tahun, {(int(umur.days)%365)//30} Bulan, {(int(umur.days)%365)%30} Hari")
print(f"Umur hari \t: {umur.days} Hari")

# print(("seribu hari lalu hari apa yah".center(50,"-")).upper())

# angka_hari = int(input("Mau hitung berapa hari yang lalu? : "))

# tahun = angka_hari // 365
# bulan = (angka_hari % 365) // 30
# hari = (angka_hari % 365) % 30
# tanggal_lalu = dt.date(tahun,bulan,hari)

# hari_ini = dt.date.today()
# waktu = (hari_ini - tanggal_lalu).days
# tahun = waktu//365
# bulan = (waktu % 365) // 30
# hari = (waktu % 365) % 30
# tanggal_hitung = dt.date(tahun,bulan,hari)


# print(f"{angka_hari} hari yang lalu adalah hari : {tanggal_hitung:%A}, {tanggal_hitung}")


