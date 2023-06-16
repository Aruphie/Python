# IF ELSE STATEMENT

angka = int(input("Masukan angka : "))

if (angka < 10) and (angka > 0) :
    print(f"{angka} adalah angka satu digit")
elif (angka < 100) and (angka > 9):
    print(f"{angka} adalah angka dua digit")
elif (angka < 1000) and (angka > 99):
    print(f"{angka} adalah angka tiga digit")
elif (angka < 10000) and (angka > 999):
    print(f"{angka} adalah angka empat digit")
else:
    print(f"{angka} gak masuk kondisi nih brooo!")

