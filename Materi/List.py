#  ===LIST===
"""
SUMMARY :
A. definisi
    > List merupakan kumpulan data bisa berbentuk string, integer, boolean atau campuan
      yang dikumpulkan dalam satu kurung siku [].
B. Membuat list
    1. menggunakan range(start, stop, step)
    2. Membuat list menggunakan for loop + if
    3. list comprehension
C. Manipulasi data pada list
    1. index[0]
    2. mengambil info jml data => len()
    3. menambahkan item pada list => data.insert(index, value)
    4. menambah list dengan list => data.extend(list)
    5. merubah data => data[0] = "data baru"
    6. meremove data => data.remove(value)
    6. meremove data terakhir => data.pop()
    7. menambah data di akhir => data.append(value)
    8. menghitung data yang sama => data.count(4)
    8. mengurutkan data => data.sort()
    9. mengambil index data => data.index(value)
    10. membalik urutan data => data.reverse()
    11. mengcopy list => data.copy()
D. Mengoutput list
    1. for loop
    2. while loop
    3. for loop dan range
    4. list comprehension
    5. enumerate

"""
# List bisa merupakan kumpulan data string, integer, boolean atau campuran
print("\n","membuat string dengan kurung[]".center(50,"_").upper())
string = ["a", "l", "v", "i", "a", "n"]
integer = [1, 2, 3, 4, 5, 6]
boolean = [True, False, False, True, False, True]
campuran = [1, False, "b", True, "a", 3]
print(f"ini list string = {string}")
print(f"ini list integer = {integer}")
print(f"ini list boolean = {boolean}")
print(f"ini list campuran = {campuran}")

## Membuat list

# Membuat list menggunakan range()
print("\n","membuat string dengan range()".center(50,"_").upper())
print(f"ini list dalam range(5) = {list(range(5))}")
print(f"ini list dalam range(1,5) = {list(range(1,5))}")
print(f"ini list dalam range(1,5,2) = {list(range(1,5,2))}") # range(start, stop, step)

# Membuat list menggunakan for loop, list comprehension
print("\n","membuat string dengan for loop".center(50,"_").upper())
print(f"i for i in range(5) = {[i for i in range(5)]}")
print(f"i for i in range(1,5,2) = {[i for i in range(1,5,2)]}")
print(f"i**3 for i in range(1,5,2) = {[i**3 for i in range(1,5,2)]}") # nilai i bisa di pangkatkan/ di operasikan

# Membuat list menggunakan for dan if
print("\n","membuat string dengan for dan if".center(50,"_").upper())
print(f"[i for i in range(5) if i != 3] = {[i for i in range(5) if i != 3]}")
print(f"[i for i in range(1,5) if i % 2 == 0] = {[i for i in range(1,5) if i % 2 == 0]}")
print(f"[i for i in range(1,5) if i % 2 != 0]= {[i for i in range(1,5) if i % 2 != 0]}") # nilai i bisa di pangkatkan/ di operasikan


## manipulasi data pada list
print("\n","manipulasi data pada list".center(50,"=").upper())

# index    0/-3     1/-2       2/-1
data = ["alvian", "raihan", "ramadan"]
#> mengambil data dari list diatas
print("\n","index".center(50,"_").upper())
print(f"ini data[0] = {data[0]}")
print(f"ini data[-1] = {data[-1]}")
print(f"ini data[1] = {data[1]}")

#> mengambil info jumlah data
print("\n","mengambil info jml data".center(50,"_").upper())
print(f"jumlah data, len(data) = {len(data)}")

#> menambahkan item pada list
print("\n","menambahkan item pada list".center(50,"_").upper())
print(f"data sbl = {data}")
data.insert(3, False)
print(f"data sesudah = {data}")

#> menambah di akhir list
print("\n","menambah di akhir list".center(50,"_").upper())
print(f"data sbl = {data}")
data.append(True)
print(f"data sesudah = {data}")

#> menambah list dengan list
print("\n","menambah list dengan list".center(50,"_").upper())
print(f"data sbl = {data}")
data.extend(["a", 1, True])
print(f"data sesudah = {data}")

#> merubah data
print("\n","merubah data".center(50,"_").upper())
print(f"data sbl = {data}")
data[3] = "Wijaya"
print(f"data sesudah = {data}")

#> meremove data => data.remove()
print("\n","meremove data".center(50,"_").upper())
print(f"data sbl = {data}")
data.remove(True)
print(f"data sesudah = {data}")

#> meremove data paling belakang => data.pop()
print("\n","meremove data paling belakang".center(50,"_").upper())
print(f"data sbl = {data}")
data.pop()
print(f"data sesudah = {data}")

#> count data => data.count(0)
print("\n","count data".center(50,"_").upper())
data_angka = [3,5,3,4,2,7,7,4,3,3,5,5,1,0]
print(f"Jumlah angka 4, data_angka.cont(3) = {data_angka.count(3)}")
print(f"Jumlah angka 4, data_angka.cont(5) = {data_angka.count(5)}")

#> ambil posisi data (index) => data.index("value")
print("\n","ambil posisi data (index)".center(50,"_").upper())
data = ["alvian", "raihan", "ramadan"]
index_alvian = data.index("alvian")
index_ramadan = data.index("ramadan")
print(f"index si alvian = {index_alvian}")
print(f"index si ramadan = {index_ramadan}")

#> mengurutkan list => sort()
print("\n","mengurutkan list".center(50,"_").upper())
data_angka = [3,5,3,4,2,7,7,4,3,3,5,5,1,0]
print(f"data angka sebelum = {data_angka}")
data_angka.sort()
print(f"data angka sesudah = {data_angka}")

#> membalik list nya => reverse()
print("\n","membalik list nya".center(50,"_").upper())
data_angka.sort()
print(f"data angka sebelum = {data_angka}")
data_angka.reverse()
print(f"data angka sesudah = {data_angka}")

#> mengcopy list => list.copy()
print("\n","mengcopy list".center(50,"_").upper())
data = ["alvian", "raihan", "ramadan"]
data_2 = data

print(f"ini id memory dari var data \n tanpa copy() : {hex(id(data))}")
print(f"ini id memory dari var data_2 \n tanpa copy() : {hex(id(data_2))}")

data_2 = data.copy()
data_2[0] = "Reza"
print(f"data sebelum = {data}")
print(f"data sesudah = {data_2}")

print(f"ini id memory dari var data \n pake copy(): {hex(id(data))}")
print(f"ini id memory dari var data_2 \n pake copy(): {hex(id(data_2))}")

        #>> kesimpulan : jika langsung disamakan seperti data_2 = data, 
        #>> maka python akan menyimpan data_2 dan data dalam memory yang sama
        #>> sehingga jika diubah salah satunya maka akan mengubah keduanya.

# NESTED LIST (list didalam list)
print("\n","nested list".center(50,"=").upper())
peserta_0 = ["Ucup", "15", "laki-laki"]
peserta_1 = ["Ujang", "11", "laki-laki"]
peserta_2 = ["Dedeh", "17", "perempuan"]

list_peserta = [peserta_0, peserta_1, peserta_2]
#> cara mengambil data di nested list
#>> Index
print("\n","Index".center(50,"_").upper())
print(list_peserta[0][0])
print(list_peserta[0][1])
print(list_peserta[0][2])

#>> for loop
print("\n","for loop".center(50,"_").upper())
for peserta in list_peserta:
    print(f"Nama \t: {peserta[0]}")
    print(f"Umur \t: {peserta[1]}")
    print(f"Gender \t: {peserta[2]}\n")

# cara mengoutput list
print("\n","Cara output list".center(50,"=").upper())

#> for loop 
print("\n","for loop".center(50,"_").upper())
peserta = ["ucup","otong","dadang","diding","dudung"]

for nama in peserta:
	print(f"Nama : {nama}")

#> while loop
print("\n","while loop".center(50,"_").upper())
panjang = len(peserta)
a = 0
while a < panjang :
      print(f"Nama : {peserta[a]}")
      a += 1

#> for loop dan range
print("\n","for loop + range".center(50,"_").upper())
for i in range(panjang):
      print(f"Nama : {peserta[i]}")

#> list comprehension
print("\n","list comprehension".center(50,"_").upper())
data = ["ucup",1,2,3,"otong"]
[print(f"data : {i}") for i in data]

angka = [10,5,4,2,6,5]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

#> enumerate
print("\n","enumerate".center(50,"_").upper())

data_list = ["ucup",1,2,3,"otong"]

for index,data in enumerate(data_list):
	print(f"index = {index}, data = {data}")


