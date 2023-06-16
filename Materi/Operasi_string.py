"""
Function pada string : 
1. Len(variable) --> untuk menghitung panjang(length) suatu string
2. min(variable) & max(variable) --> item paling kecil & paling besar dari ASCII CODE --> ord("A") | chr(92)
3. var.count("a") --> menghitung jumlah huruf a pada var
4. var.upper(), var.lower(), capitalize() --> mengubah string var menjadi kapital & huruf kecil
5. isX method --> untuk mengecek string
    isupper() & islower() --> mengecek apakah semua katanya huruf besar | kecil
    isalpha() --> untuk mengecek semuanya huruf
    isalnum() --> huruf & angka
    isdecimal() --> angka saja
    isspace() --> spasi, tab, newline \n
    istittle() --> semua kata dimulai dengan huruf besar
6. var.startswitch("Kataawal") --> mengecek apakah kata awalnya sama
7. var.endswitch("Kataakhir") --> mengecek apakah kata akhirnya sama
8. "".join(list) & var.split("") --> menggabungkan atau memisahkan kata pada list
9. ljust(), rjust(), center() --> left justify, right justify, center
10. strip() --> menghilangkan tanda

Operator pada string :
1.  (+) --> untuk menyatukan string
    (*) --> untuk mengulang string
2. in / not in --> menngecek apakah ada komponen char atau string dalam string.
    ex :    a = "Lenovo"
            print("L" in a) --> True
3. Indexing ('variable[angka]')
    ex :    var = Lenovo 
                  012345
            print(var[0]) --> L
            print(var[0:3]) --> Len
            print(var[3:6]) --> ovo
            print(var[0:6:2]) --> Lnv
4. List ('var = ["nama", "aku", "alvian"]')
    ex :    var = ["nama", "aku", "alvian"]
            gabung = " ".join()
"""
#penggabungan dan pemisahan kata pada list :
pisah = ["nama", "aku", "alvian"]
print(" ".join(pisah))
sambung = "namaehmakuehmalvian"
print(sambung.split("ehm"))

#penggunaan rjust(), ljust(), dan center()
pembatas = "kanan".rjust(50,"=")
print(pembatas.upper())
pembatas = "Kiri".ljust(50,"=")
print(pembatas.upper())
pembatas = "tengah".center(50,"=")
print(pembatas.upper())
pembatas = "TENGAH".strip("=")
print(pembatas.capitalize())
