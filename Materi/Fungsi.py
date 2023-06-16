import os

'''
=== Template fungsi ===
def nama_fungsi(argumen1,argumen2):
       badan fungsi
       return output
'''

# y = f(x) = x**2 

#       f   (x)
def kuadrat(angka):
    '''Fungsi Kuadrat'''
    return angka**2
#     y     x**2
print(kuadrat(9))

# argumen default     ---vvvv---            ---vvv---
def say_hi(nama = 'kamu',kabar = 'apa kabar nich?'):
    '''Fungsi say_hi'''
    print(f"halo {nama}, {kabar}")

say_hi()
say_hi('ujang', 'kumaha damang?')

# contoh project
'''
fungsi untuk menentukan luas dan keliling pesegi panjang :
> while True :
    - header
    - input
    - panggil fungsi
    - output
'''

def header():
    '''Fungsi Header'''
    os.system('cls')

    print(f"{'APLIKASI PENGHITUNG LUAS':^50}")
    print(f"{'DAN KELILING PERSEGI':^50}")
    print("-"*50)

def input_user():
    '''Fungsi Input'''
    input_panjang = int(input("Panjang \t: "))
    input_lebar = int(input("Lebar \t\t: "))
    return input_panjang,input_lebar

def hitung_luas(panjang,lebar):
    '''Fungsi Luas'''
    return panjang * lebar

def hitung_keliling(panjang,lebar):
    '''Fungsi Keliling'''
    return 2*(panjang + lebar)

def output():
    '''Fungsi Output'''
    print("HASIL".center(20,'-'))
    print(f"Keliling \t= {keliling:,}")
    print(f"Luas \t\t= {luas:,}")
    print("\n")


while True :
    header()
    panjang,lebar = input_user()

    keliling = hitung_keliling(panjang,lebar)
    luas = hitung_luas(panjang,lebar)

    output()

    isContinue = input("Mau lanjut? (y/n) : ")
    if isContinue == 'n':
        break

print("\n")
print("--- AKHIR DARI PROGRAM TERIMAKASIH :) ---")

