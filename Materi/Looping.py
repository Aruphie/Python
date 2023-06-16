# Looping menggunakan For Loop
print(("Looping dengan For Loop".center(50,"=")).upper(), "\n")

### Pengenalan range()
print("pengenalan range()".rjust(50,"_"), "\n")
print(f"ini adalah range(6) --> {list(range(6))}")
print(f"ini adalah range(9) --> {list(range(9))}")

## menggunakan range
print("\n", "FOR LOOP pake range()".rjust(50,"_"))

for i in range(5):
    print(f"i = {i}")

## menggunakan List
print("\n", "FOR LOOP pake List".rjust(50,"_"))

list = [1, 2, 3, 4, 5]

for a in list:
    print(f"a = {a}")

## menggunakan string 
print("\n", "FOR LOOP pake string".rjust(50,"_"))

str = "alvian"

for z in str :
    print(f"z = {z}")

# Looping dengan menggunakaan while loop
print("\n", ("Looping dengan While Loop".center(50,"=")).upper())

a = 0

while a < 5:
    a += 1
    print(f"a = {a}")

## pengenalan control flow : pass, continue, break
print("\n", ("Control flow".center(50,"=")).upper())

### pass
print("\n", "Pass".rjust(50,"_"))
a = 0

while a < 5:
    a += 1
    if a == 3:
        pass # dummy, tidak bakal di eksekusi
        # print("kamu kece!")

    print(f"a = {a}")

### continue
print("\n", "Continue".rjust(50,"_"))
a = 0

while a < 5:
    a += 1
    if a == 3:
        continue # langsung kembali ke atas tanpa mengeksekusi syntax di bawahnya
        # print("kamu kece!")

    print(f"a = {a}")
    
### break
print("\n", "Break".rjust(50,"_"))
a = 0

while a < 5:
    a += 1
    if a == 3:
        break # langsung berhenti
        # print("kamu kece!")

    print(f"a = {a}")
    

