from CRUD.Database import DB_NAME
from CRUD.Operation import random_choice,time_console,check,create,read,update,delete


# Check data
def check_data():
    pk = random_choice(6)
    waktu = time_console()

    try:
        with open(DB_NAME,'r') as file:
            file.read()
    except:
        print("\nDATA BELUM DI BUAT! SILAHKAN MASUKAN DATA BARU! \n")
        judul = input("Judul\t: ")
        penulis = input("Penulis\t: ")
        while True:
            try:
                tahun = int(input("Tahun\t: "))
                if len(str(tahun)) > 4 or len(str(tahun)) < 4 :
                    print('Tahun di luar jangkauan!')
                    continue
                break
            except ValueError:
                print("Tahun harus berisi angka!")
    
        check(pk,waktu,judul,penulis,tahun)

# Create
def create_data():
    # variable
    pk = random_choice(6)
    waktu = time_console()

    # input
    print("\nSILAHKAN MASUKAN DATA YANG AKAN DIBUAT : \n")
    judul = input("Judul\t: ")
    penulis = input("Penulis\t: ")
    while True:
        try:
            tahun = int(input("tahun\t: "))
            if len(str(tahun)) != 4 :
                print('Tahun di luar jangkauan!')
                continue
            break
        except ValueError:
            print("Tahun harus berisi angka!")

    create(pk,waktu,judul,penulis,tahun)
    print("\nBERIKUT ADALAH DATA BARU ANDA : ")
    read_data()

# Read
def read_data():
    content = read()

    print('\n'+'='*100)
    print(f"{'No. ':4} | {'Judul':40} | {'Penulis':40} | {'Tahun':5}")
    print('-'*100)

    for index,data_buku in enumerate(content):
        buku = data_buku.split(' | ')
        judul, penulis, tahun = buku[2], buku[3], buku[4]
        print(f"{index+1:^4} | {judul:.40} | {penulis:.40} | {tahun:.5}",end='')
    print('='*100)

# Update
def update_data():
    read_data()
    while True:
        print('\nSILAHKAN PILIH NO.BUKU YANG INGIN DI UPDATE!')
        no_buku = int(input("Nomor Buku : "))
        data_buku = read(index=no_buku)
        
        if data_buku :
            break
        else :
            print('Nomor tidak valid')
    
    data_break = data_buku.split(' | ')
    pk = data_break[0]
    waktu = data_break[1]
    judul = data_break[2]
    penulis = data_break[3]
    tahun = data_break[4][:-1]

    # Update data 
    while True :
        print('\n'+'-'*100)
        print(f"Silahkan pilih data yang mau di update!")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:}")
        print(f"4. Exit\n")

        # memilih untuk user update
        opsi = input("Pilih apa yang akan di update : ")
        match opsi :
            case '1' : judul = input('Judul\t: ')
            case '2' : penulis = input('Penulis\t: ')
            case '3' : 
                while True:
                    try:
                        tahun = input("Tahun\t: ")
                        if len(tahun) != 4 :
                            print('Tahun di luar jangkauan!')
                            continue
                        break
                    except ValueError:
                        print("Tahun harus berisi angka!")
            case '4' : break
            case _ : print('Opsi tidak cocok!')
        
        print('\n'+'-'*100)
        print(f"Berikut adalah data baru anda!")
        print(f"Judul\t: {judul:.40}")
        print(f"Penulis\t: {penulis:.40}")
        print(f"Tahun\t: {tahun}\n")

        is_done = input('Langsung simpan? (y/n) : ')
        match is_done :
            case 'y'|'Y': break

    update(no_buku,pk,waktu,judul,penulis,tahun)
        
# Delete
def delete_data():
    read_data()
    while True:
        print('\nSILAHKAN PILIH NO.BUKU YANG INGIN DI DELETE!')
        no_buku = int(input("Nomor Buku : "))
        data_buku = read(index=no_buku)
        
        if data_buku :
            data_break = data_buku.split(' | ')
            judul = data_break[2]
            penulis = data_break[3]
            tahun = data_break[4][:-1]

            print('\n'+'-'*100)
            print(f"Berikut adalah data yang akan di hapus!")
            print(f"Judul\t: {judul:.40}")
            print(f"Penulis\t: {penulis:.40}")
            print(f"Tahun\t: {tahun}\n")

            is_done = input('Yakin akan di hapus? (y/n) : ')
            match is_done :
                case 'y'|'Y': 
                    delete(no_buku)
                    break
        else :
            print('Nomor tidak valid')
    
    print("Data berhasil di hapus")