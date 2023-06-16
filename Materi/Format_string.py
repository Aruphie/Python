# format string
print("FORMAT STRING".center(50,"="))

# contoh generik
# string
nama = "Alvian"
Format_nama = f"Nama saya, {nama}"
print(Format_nama, "\t\t--> String")

# boolean
boolean = True
Format_boolean = f"Saya ganteng, {boolean}"
print(Format_boolean, "\t\t--> boolean")

# angka
angka = 2500000
print(f"angka \t: {angka}", "\t\t--> angka")
print(f"angka \t: {angka:,}", "\t\t--> angka ordo ribuan")
print(f"angka \t: {angka:d}", "\t\t--> angka bulat")

# angka desimal
desimal = 2005.2567491
print(f"angka \t: {desimal:.3f}", "\t\t--> angka desimal")
print(f"angka \t: {desimal:09.2f}", "\t\t--> leading zero")

# menampilkan tanda plus(+) / min(-)
plus = 10
minus = -20.256789
print(f"Plus \t: {plus:+d}", "\t\t\t--> angka plus")
print(f"Minus \t: {minus:+.2f}", "\t\t--> angka minus")

# memformat persen(%)
persen = 0.035
print(f"Persen \t: {persen:.1%}", "\t\t\t--> persen")

# melakukan operasi aritmatika dalam format string
angka1 = 5
angka2 = 2
print(f"Hasil\t: {angka1 + angka2}", "\t\t\t--> penjumlahan")
print(f"Hasil\t: {angka1 * angka2}", "\t\t\t--> perkalian")
print(f"Hasil\t: {(angka1 ** angka2)/2}", "\t\t\t--> campuran")

# format angka lain (binary, octal, hexadinamical)
angka = 125
print(f"Binary\t: {bin(angka)}", "\t\t--> binary")
print(f"Octal\t: {oct(angka)}", "\t\t--> octal")
print(f"Hex\t: {hex(angka)}", "\t\t\t--> hexadinamical")

# Mengatur alignment di format string
print("MENGATUR ALIGNMENT".center(50,"="))

#Data
Nama = "Alvian Raihan Ramadan"
Umur = 17
Tinggi = 175.5
Sepatu = 44

# string multiline menggunakan new line
print("multiline (new line)".rjust(50,"_"))
print(f"Nama \t: {Nama} \nUmur \t: {Umur} \nTinggi \t: {Tinggi} \nSepatu \t: {Sepatu}" )

# string multiline menggunakan kutip tiga
print("multiline (kutip tiga)".rjust(50,"_"))
print(f"""Nama \t: {Nama}
Umur \t: {Umur}
Tinggi \t: {Tinggi}
Sepatu \t: {Sepatu}
""")
