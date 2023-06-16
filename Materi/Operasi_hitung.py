""" 
prioritas dalam operasi hitung di python :
1. ()
2. Eksponen
3. Perkalian, Pembagiam, Modulus, Floor Division
4. Penjumlahan dan pengurangan

"""

a = 10
b = 7

#Penjumlahan (+)
jumlah = a + b 
print(a, '+', b, '=', jumlah )

#Pengurangan (-)
jumlah = a - b 
print(a, '-', b, '=', jumlah )

#Perkalian (*)
jumlah = a * b 
print(a, '*', b, '=', jumlah )

#Pembagian (/)
jumlah = a / b 
print(a, '/', b, '=', jumlah )

#Floor division (//)
jumlah = a // b 
print(a, '//', b, '=', jumlah )

#Eksponen (**)
jumlah = a ** b 
print(a, '*', b, '=', jumlah )

#Modulus (%)
jumlah = a % b 
print(a, '%', b, '=', jumlah )

#Operasi hitung campuran
print("\n===OPERASI HITUNG CAMPURAN===\n")
jumlah = a * b + a - b ** a / b % a // b
print(a, '*', b, '+', a, '-', b, '**', a, '/', b, '%', a, '//', b, ' = ', jumlah)