# tuples & sets
tuples = (1,2,3,4,5,6,7,8) # tidak bisa diubah
sets = {1,2,3,4,5,6,7,8} # tidak memiliki index / Himpunan

dictionary = {
    #  KEY   :  VALUE
    "string" : "ucup",
    "integer" : 10,
    "Boolean" : True,
    "nested list" : ["ucup", 1, True],
    "another_dictionary" : {"ujang", 10, False}
}

string = dictionary["string"]
nested_list = dictionary["nested list"]
print(f"\ndictionary['string'] : {string} \n")
print(f"dictionary['nested list'] : {nested_list} \n")

# OPERASI PADA DICTIONARY

#> 1. mencaritau panjang -> len()
print(f"Panjang : {len(dictionary)} \n")

#> 2. mengecek key exist atau tidak -> key in dictionary
key = "string"
print(f"Check_KEY 'string' : {key in dictionary} \n")

#> 3. mengakses value (read) dengan get
print(dictionary["string"])
print(dictionary.get("string"))
print(dictionary.get("kis","key tidak ditemukan")) # cek key dengan message tidak ditemukan

#> mengupdate data
dictionary["string"] = "ucup si ganteng"
print(dictionary)
dictionary["integer"] = "asep si kasyep"
print(dictionary,"\n")

dictionary.update({"string":"ucup surucup"})
print(dictionary)
dictionary.update({"Alvian":"Alvian si kweren"}) # kalau key nya tidak ada berarti nambah baru
print(dictionary,"\n")

#> mendelete data pada dictionary
del dictionary["Alvian"]
print(dictionary, "\n")

# looping dictionary
print(f"Loop dictionary".center(50,"=").upper(), "\n")
dictionary = {
    #  KEY   :  VALUE
    "string" : "ucup",
    "integer" : 10,
    "Boolean" : True,
    "nested list" : ["ucup", 1, True],
    "another_dictionary" : {"ujang", 10, False}
}

for data in dictionary : # outputnya keys
    print(f" apa = {data}")

for key in dictionary.keys() :
    print(f" Key = {key}")

for value in dictionary.values() :
    print(f" Values = {value}")

for item in dictionary.items():
    print(f" item = {item}")

for key,value in dictionary.items():
    print(f" key = {key} | value = {value}")


# Copy & pop dictioary
dictionary = {
    #  KEY   :  VALUE
    "string" : "ucup",
    "integer" : 10,
    "Boolean" : True,
    "another_dictionary" : {"ujang", 10, False}
}

dictionary_2 = dictionary.copy()
dictionary.update({"string":"Ujang"})
print(f"Dictionary = {dictionary}")
print(f"Dictionary_2 = {dictionary_2}\n")

pop = dictionary.pop("string") # output nya values aja tapi yang pindah itemsnya
print(f"pop = {pop}")
print(dictionary)

popitem = dictionary.popitem() # outputnya items
print(f"popitem = {popitem}")
print(dictionary)



