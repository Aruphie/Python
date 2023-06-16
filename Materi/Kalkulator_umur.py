# MEMBUAT KALKULATOR UMUR XD
import datetime
import os

def header():
    '''fungsi header'''
    os.system('cls')
    print(f"{'APLIKASI PENGHITUNG UMUR 2.0':^50}")
    print('-'*50)
    print("Silahkan masukan tanggal lahir anda :) ")

def data_input():
    '''fungsi data input'''
    #masukan tanggal lahir kamu <3
    tanggal = int(input("Tanggal \t: "))
    bulan = int(input("Bulan \t\t: "))
    tahun = int(input("Tahun\t\t: "))
    return tanggal,bulan,tahun

# ubah selisih_hari menjadi bentuk tahun, bulan dan hari
def hitung_selisih(tanggal,bulan,tahun):
    '''fungsi hitung selisih hari'''
    # hitung berapa hari berlalu sejak kamu lahir 
    tanggal_lahir = datetime.datetime(tahun,bulan,tanggal)
    hari_ini = datetime.datetime.today()
    selisih = hari_ini - tanggal_lahir
    selisih_hari = selisih.days
    return selisih_hari,tanggal_lahir

def hitung_umur(selisih_hari):
    '''fungsi hitung umur'''
    # ubah dalam tahun, bulan dan hari
    umur_tahun = selisih_hari // 365
    umur_bulan = (selisih_hari % 365) // 30
    umur_hari = (selisih_hari % 365) % 30
    return umur_hari,umur_bulan,umur_tahun

# Output
def output(tanggal_lahir,selisih_hari):
    '''fungsi output'''
    print("\n"," HASIL ".center(50,"-").upper())
    print(f"You were born in {tanggal_lahir:%A}, {tanggal_lahir:%d} {tanggal_lahir:%B} {tanggal_lahir:%Y}")
    print(f"Umurmu {umur_tahun} tahun, {umur_bulan} bulan, {umur_hari} hari")
    print(f"atau tepatnya selama {selisih_hari} hari")
    
def footer():
    '''fungsi penutup'''
    print("\n")
    print("=== PROGRAM SELESAI TERIMAKASIH ===")
    print("\n")

while True:
    header()

    tanggal,bulan,tahun = data_input()
    selisih_hari,tanggal_lahir = hitung_selisih(tanggal,bulan,tahun)
    umur_hari,umur_bulan,umur_tahun = hitung_umur(selisih_hari)

    output(tanggal_lahir,selisih_hari)

    print("\n")
    lanjut = input("MAU LANJUT?(y/n) : ")
    if lanjut == 'n':
        break


footer()
