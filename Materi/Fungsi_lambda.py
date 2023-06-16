import os
os.system('cls')
# variable = lambda argument:assignment
# variable(argument)

# contoh simple :
jumlah = lambda angka_1,angka_2 : angka_1 + angka_2
hasil = jumlah(5,10)
print(hasil)

# kegunaan nya :
#> 1. sort sebuah list :
data_nama = ['eka','stephani','jaeudin','arji','bujang']
data_nama.sort(key=lambda nama:len(nama)) # sort berdasarkan panjang nama
print(data_nama)

#> 2. filter sebuah list :
angka = [2,1,3,4,2,5,7,8,6,9,5]

data_genap = list(filter(lambda x:(x%2==0),angka))
print(data_genap)

data_ganjil = list(filter(lambda x:(x%2!=0),angka))
print(data_ganjil)

#> 3. Anonymous function / currying (Haskel Currying)
def pangkat(n):
    return lambda x:x**n

pangkat2 = pangkat(2)
pangkat2_dari_5 = pangkat2(5)
print(pangkat2_dari_5)

print(pangkat(3)(2))

