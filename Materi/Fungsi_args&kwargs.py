# type hints pada fungsi
            #type hints ---vvv-- --vvv--
def tambah(angka_1:int,angka_2:int) -> int: 
    return angka_1 + angka_2
print(tambah(3,4))

# *args & **kwargs
#> contoh *args 1 :
def fungsi(*args) :
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} memiliki tinggi {tinggi} dan berat {berat}")

fungsi('ucup', 175, 65)

#> contoh *args 2 :
def jumlah(*data):
    # datanya adalah tuple bisa di iterasi
    output = 0
    for angka in data:
        output += angka

    return output

hasil = jumlah(1,7,5,4)
print(hasil)

#> contoh **kwargs
def fungsi_2(**kwargs) :
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    print(f"{nama} memiliki tinggi {tinggi} dan berat {berat}")

fungsi_2(nama = 'ucup', tinggi = 155, berat =67)

#> contoh campur
def kalkulator(*args,**kwargs):
    output = 0

    if kwargs['option'] == 'tambah':
        for angka in args:
            output += angka
        print(output)
    
    elif kwargs['option'] == 'kali':
        output = 1
        for angka in args:
            output *= angka
        print(output)

    else:
        print("maaf belum bisa bro!")

kalkulator(7,6,5,8,6,option = 'tambah')
kalkulator(7,6,5,8,6,option = 'kali')
    
