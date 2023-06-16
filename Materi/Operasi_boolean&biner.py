#=========OPERASI LOGIKA atau BOOLEAN=============
"""
Macam-macam operasi boolean :
1. NOT (~)
2. OR (|)
3. AND (&)
4. XOR (^) --> akan bernilai 'True' jika salah satu 'True'

"""
print('=========OPERASI LOGIKA atau BOOLEAN=============')
print('\n_______NOT_________')
a = False
b = True
Hasil = not a
print ('NOT ', a, ' = ', Hasil )
Hasil = not b
print ('NOT ', b, ' = ', Hasil )

print('\n_______OR_________')
a = False
b = True
Hasil = a or b
print (a, ' OR ', b, ' = ', Hasil )
a = True 
b = False
Hasil = a or b
print (a, '  OR ', b, '= ', Hasil )
a = True
b = True
Hasil = a or b
print (a, '  OR ', b, ' = ', Hasil )
a = False
b = False
Hasil = a or b
print (a, ' OR ', b, '= ', Hasil )

print('\n_______AND_________')
a = False
b = True
Hasil = a and b
print (a, ' AND ', b, ' = ', Hasil )
a = True 
b = False
Hasil = a and b
print (a, '  AND ', b, '= ', Hasil )
a = True
b = True
Hasil = a and b
print (a, '  AND ', b, ' = ', Hasil )
a = False
b = False
Hasil = a and b
print (a, ' AND ', b, '= ', Hasil )

print('\n_______XOR_________')
a = False
b = True
Hasil = a ^ b
print (a, ' XOR ', b, ' = ', Hasil )
a = True 
b = False
Hasil = a ^ b
print (a, '  XOR ', b, '= ', Hasil )
a = True
b = True
Hasil = a ^ b
print (a, '  XOR ', b, ' = ', Hasil )
a = False
b = False
Hasil = a ^ b
print (a, ' XOR ', b, '= ', Hasil )

#============OPERASI BINER==========
print('\n=================BINER=================')
a = 1
print('Nilai a : ', a, 'biner : ', format(a, '08b'))
#==========NOT==========
print('\n=================NOT=================')
a = ~a
print('Nilai a : ', a, 'biner : ', format(a, '08b'))
#==========OR==========
print('\n=================OR=================')
a = 1
b = 3
c = a | b
print('Nilai a :', a, 'biner : ', format(a, '08b'))
print('Nilai b :', b, 'biner : ', format(b, '08b'))
print('Nilai c :', c, 'biner : ', format(c, '08b'))
d = False
print('Nilai d :', d, 'biner : ', format(d, '08b'))
d |= True
print('Nilai d |= True :', d, 'biner : ', format(d, '08b'))
d = False
d |= False
print('Nilai d |= False :', d, 'biner : ', format(d, '08b'))

#==========AND==========
print('\n=================AND=================')
a = 1
b = 3
c = a & b
print('Nilai a :', a, 'biner : ', format(a, '08b'))
print('Nilai b :', b, 'biner : ', format(b, '08b'))
print('Nilai c :', c, 'biner : ', format(c, '08b'))
#==========XOR==========
print('\n=================XOR=================')
a = 1
b = 3
c = a ^ b
print('Nilai a :', a, 'biner : ', format(a, '08b'))
print('Nilai b :', b, 'biner : ', format(b, '08b'))
print('Nilai c :', c, 'biner : ', format(c, '08b'))


