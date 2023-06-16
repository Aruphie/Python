# MEMBUAT SEGITIA DENGAN MENGGUNAKAN LOOPING

## Menggunakan for loop :
tingkat = int(input("mau berapa tingkat? : "))
tingkat *= 4
dummy = 0

for segitiga in range(tingkat) :
    dummy += 1

    if dummy%4 == 1 :
        print(("F" * dummy).center(tingkat," "))
    

## Menggunakan while loop :
tingkat = int(input("mau berapa tingkat? : "))
tingkat *= 4
dummy = 0

while True :
    dummy += 1

    if dummy % 4 == 1 :
        print(("H"*dummy).center(tingkat," "))

    elif dummy == tingkat :
        break