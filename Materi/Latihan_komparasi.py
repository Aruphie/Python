#LATIHAN KOMPARASI BOOLEAN
UserInput = float(input('Masukan angka : '))
#-----0+++++++5--------8+++++++11---------
Lebih_nol = UserInput > 0
Kurang_Lima = UserInput < 5
lebih_delapan = UserInput > 8
Kurang_sebelas = UserInput < 11

hasil = (Lebih_nol and Kurang_Lima) or (lebih_delapan and Kurang_sebelas)
print(hasil)

#+++++0-------5+++++++++8--------11+++++++++
UserInput2 = float(input('Masukan angka :'))
Kurang_nol = UserInput2 < 0
Lebih_lima = UserInput2 > 5
Kurang_delapan = UserInput2 < 8
Lebih_sebelas = UserInput2 > 11

hasil2 = Kurang_nol or (Lebih_lima and Kurang_delapan) or Lebih_sebelas
print(hasil2)