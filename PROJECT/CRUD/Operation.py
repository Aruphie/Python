import shutil
import random
import string
import time
import os
from CRUD.Database import TEMPLATE,DB_NAME

# Variable
data = TEMPLATE.copy()

# random_console
def random_choice(n:int) -> int :
    return ''.join(random.choice(string.ascii_letters) for i in range(n))

# time_console
def time_console():
    return time.strftime('%d/%m/%Y %H-%M-%S')

# check
def check(pk,waktu,judul,penulis,tahun):
    data['pk'] = pk
    data['waktu'] = waktu
    data['judul'] = judul + TEMPLATE['judul'][len(judul):]
    data['penulis'] = penulis + TEMPLATE['penulis'][len(penulis):]
    data['tahun'] = tahun

    try:
        with open(DB_NAME,'a',encoding='utf-8') as file:
            file.write(f"{data['pk']} | {data['waktu']} | {data['judul']} | {data['penulis']} | {data['tahun']}\n")
    except:
        print('GAGAL MEMUAT DATA!! Operation/check()')
    
# create
def create(pk,waktu,judul,penulis,tahun):
    data['pk'] = pk
    data['waktu'] = waktu
    data['judul'] = judul + TEMPLATE['judul'][len(judul):]
    data['penulis'] = penulis + TEMPLATE['penulis'][len(penulis):]
    data['tahun'] = tahun

    try:
        with open(DB_NAME,'a',encoding='utf-8') as file:
            file.write(f"{data['pk']} | {data['waktu']} | {data['judul']} | {data['penulis']} | {data['tahun']}\n")
    except:
        print('GAGAL MEMUAT DATA!! Operation/create')
    
# read
def read(**kwargs):
    try:
        with open(DB_NAME,'r') as file:
            content = file.readlines()
            jml_buku = len(content)
            if 'index' in kwargs:
                index_buku = (kwargs['index'])-1
                if index_buku < 0 or index_buku > jml_buku :
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print('MEMBACA DATABASE ERROR')
        return False       

# update
def update(no_buku,pk,waktu,judul,penulis,tahun):
    data['pk'] = pk
    data['waktu'] = waktu
    data['judul'] = judul + TEMPLATE['judul'][len(judul):]
    data['penulis'] = penulis + TEMPLATE['penulis'][len(penulis):]
    data['tahun'] = tahun

    data_str = f"{data['pk']} | {data['waktu']} | {data['judul']} | {data['penulis']} | {data['tahun']}\n"
    panjang_data = len(data_str)

    try:
        with open(DB_NAME,'r+',encoding='utf-8') as file :
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print("ERROR DALAM UPDATE DATA!! ")
        return False

# delete
def delete(no_buku):
    try:
        with open(DB_NAME,'r') as file:
            count = 0
            while True :
                content = file.readline()
                if len(content) == 0: 
                    break
                elif count == (no_buku - 1): 
                    pass
                else:
                    with open('data_temp.txt','a',encoding='utf-8') as temp_file:
                        temp_file.write(content)
                count += 1
    except:
        print('Database Error!')

    if os.path.exists('data.txt'):
        shutil.move('data.txt', 'backup_data.txt')
    os.rename('data_temp.txt', 'data.txt')

    

