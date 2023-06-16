#==========================PROGRAM SUHU FAHRENHEIT============================
print('====PROGRAM KONVERSI SUHU FAHRENHEIT====\n')

Fahrenheit = float(input('Masukan suhu Fahrenheit : '))
print('Suhu Fahrenheit : ', Fahrenheit)

#Celcius
print('___CELCIUS___')
Celcius = (5/9)*(Fahrenheit - 32)
print('\n Suhu dalam Celcius adalah : ', Celcius, 'Celcius\n')

#Reamur
print('___REAMUR___')
Reamur = (4/9)*(Fahrenheit - 32)
print('\n Suhu dalam Reamur adalah : ', Reamur, 'Reamur\n')

#Kelvin
print('___KELVIN___')
Kelvin = Celcius + 273
print('\n Suhu dalam Kelvin adalah : ', Kelvin, 'Kelvin\n')

#===========================PROGRAM SUHU KELVIN==============================

print('====PROGRAM KONVERSI SUHU KELVIN====\n')

Kelvin = float(input('Masukan suhu Kelvin : '))
print('Suhu Kelvin : ', Kelvin)

#Celcius
print('___CELCIUS___')
Celcius = (Kelvin - 273.0)
print('\n Suhu dalam Celcius adalah : ', Celcius, 'Celcius\n')

#Reamur
print('___REAMUR___')
Reamur = (4/5) * Celcius
print('\n Suhu dalam Reamur adalah : ', Reamur, 'Reamur\n')

#Fahrenheit
print('___FAHRENHEIT___')
Fahrenheit = ((9/5) * Celcius) + 32.0
print('\n Suhu dalam Fahrenheit adalah : ', Fahrenheit, 'Fahrenheit\n')