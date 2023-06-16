# === MEMBUAT LIST BUKU ===

list_buku = []
while True :
    #> input User :
    judul = input("\nMasukan judul buku \t: ")
    penulis = input("Masukan penulis \t: ")

    #> Masukan input dalam list
    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    #> print list_buku
    print("="*20)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | judul : {buku[0]} | Penulis : {buku[1]}")

    #>stop
    stop = input("\napakah ada lagi? (y/n) \t: ")
    if stop == "n":
       break

print("program selesai")