"""
Ada beberapa bentuk komparasi :
1. Lebih dari (>)
2. Kurang dari (<)
3. Lebih dari sama dengan (>=)
4. Kurang dari sama dengan (<=)
5. sama dengan (==)
6. Tidak sama dengan (!=)
7. is       \ untuk membandingkan objek identity (hex(id()))
8. is not   / ex : a is b |  a is not b

hasil dari komparasi selalu boolean (True/False)
"""

#Lebih dari (>)
print('====LEBIH DARI===')
print(3 > 2)
print(3 > 5)

#Lebih dari sama dengan (>=)
print('====LEBIH DARI SAMA DENGAN===')
print(3 >= 5)
print(3 >= 5)

#Kurang dari (>)
print('====KURANG DARI===')
print(3 < 5)
print(3 < 5)

#Kurang dari sama dengan (>=)
print('====KURANG DARI SAMA DENGAN===')
print(3 <= 5)
print(3 <= 5)

#Sama dengan (==)
print('====SAMA DENGAN===')
print(3 == 5)
print(3 == 5)

#Tidak sama dengan (!=)
print('====TIDAK SAMA DENGAN===')
print(3 != 5)
print(3 != 5)

#is & is not
print('====IS & IS NOT===')
a = 5
b = 6

print('Identity a : ', hex(id(a)), '\n',
      'Identity b : ', hex(id(b)), '\n', 
      'a is b = ', a is b)
print('Identity a : ', hex(id(a)), '\n',
      'Identity b : ', hex(id(b)), '\n', 
      'a is not b = ', a is not b)