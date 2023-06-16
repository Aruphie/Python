import datetime
siswa = {}
TANGGAL_LAHIR = input("Tanggal lahir\n(DD-MM-YYYY) \t: ")
siswa['lahir'] = datetime.datetime.strptime(TANGGAL_LAHIR, '%d-%m-%Y').strftime("%d/%m/%y")
print(siswa)
    