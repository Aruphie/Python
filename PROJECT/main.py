import os
from CRUD.Exsecution import check_data,create_data,read_data,update_data,delete_data

if __name__ == '__main__':

    device = os.name
    match device:
        case 'posix': os.system('clear')
        case 'nt': os.system('cls')
    
    check_data()

    while True:
        device = os.name
        match device:
            case 'posix': os.system('clear')
            case 'nt': os.system('cls')

        # HEADER 
        print('='*100)
        print('SELAMAT DATANG DI PROGRAM CRUD'.center(100))
        print('(Create, Read, Update, Delete)'.center(100))
        print('='*100)

        # BODY
        print(''' Pilih berdasarkan opsi di bawah ini : 
        1. Create Data
        2. Read Data
        3. Update Data
        4. Delete Data
        5. Exit Program
        ''')

        opsi = int(input("Masukan opsi \t: "))
        match opsi:
            case 1 : create_data() 
            case 2 : read_data()
            case 3 : update_data()
            case 4 : delete_data()
            case 5 : 
                print('\nTERIMAKASIH SUDAH MAMPIR KAKAAAAK!\n') 
                break

        is_done = input("\nKeluar dari program? (y/n) : ")
        match is_done:
            case 'y'|'Y' :
                print('\nTERIMAKASIH SUDAH MAMPIR KAKAAAAK!\n') 
                break
        
        














