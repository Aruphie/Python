def tambah(*args):
    hasil = 0
    for angka in args:
        hasil += angka
    return hasil

def kali(*arg):
    hasil = 1
    for angka in arg:
        hasil *= angka
    return hasil
