# read data.txt
with open('data.txt','r') as file:
    nama_u = file.readlines()
    print(nama_u)

# menambah data.txt   v--> a untuk append
with open('data.txt','a',encoding='utf-8') as file:
    file.writelines('Abidin')
    print(file)

# menulis tapi mereset data.txt
with open('data.txt','w',encoding='utf-8') as file:
    file.write('SEMUAANYA HILANGGGG!!!')
    print(file)



