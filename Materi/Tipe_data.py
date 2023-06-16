"""
Tipe-tipe data :
1. Integer
2. String
3. Float
4. Boolean
____Tipe-tipe Khusus____ : (Episode 5)
5. data complex (Imajiner)
6. data dari bahasa C
"""



#INTEGER
print('====INTEGER====')
Data_Integer = 10
print('Data Integer: ', Data_Integer, ' , Tipe : ', type(Data_Integer))
print('vvvvvvvvv')

Data_String = str(Data_Integer)
Data_Float = float(Data_Integer)
Data_Bool = bool(Data_Integer)

print('Data Float: ', Data_Float, ' , Tipe : ', type(Data_Float))
print('Data String: ', Data_String, ' , Tipe : ', type(Data_String))
print('Data Bool: ', Data_Bool, ' , Tipe : ', type(Data_Bool))

#FLOAT
print('\n')
print('====FLOAT====')
Data_Float = 0
print('Data Float: ', Data_Float, ' , Tipe : ', type(Data_Float))
print('vvvvvvvvv')

Data_String = str(Data_Float)
Data_Integer = int(Data_Float)
Data_Bool = bool(Data_Float)

print('Data String : ', Data_String, ' , Tipe : ', type(Data_String))
print('Data Integer : ', Data_Integer, ' , Tipe : ', type(Data_Integer))
print('Data Bool : ', Data_Bool, ' , Tipe : ', type(Data_Bool))

#BOOLEAN
print('\n')
print('====BOOLEAN====')
Data_Bool = True
print('Data Bool: ', Data_Bool, ' , Tipe : ', type(Data_Bool))
print('vvvvvvvvv')

Data_String = str(Data_Bool)
Data_Integer = int(Data_Bool)
Data_Float = float(Data_Bool)

print('Data String : ', Data_String, ' , Tipe : ', type(Data_String))
print('Data Integer : ', Data_Integer, ' , Tipe : ', type(Data_Integer))
print('Data Float : ', Data_Float, ' , Tipe : ', type(Data_Float))

#STRING
print('\n')
print('====STRING====')
Data_String = "0"
print('Data Strinng: ', Data_String, ' , Tipe : ', type(Data_String))
print('vvvvvvvvv')

Data_Bool = bool(Data_String) #bool akan bernilai 'False' jika string kosong & bernilai 'True' jika ada isinya
Data_Integer = int(Data_String) #ini akan erorr jika string berisi huruf
Data_Float = float(Data_String) #ini akan erorr jika string berisi huruf

print('Data Bool : ', Data_Bool, ' , Tipe : ', type(Data_Bool))
print('Data Integer : ', Data_Integer, ' , Tipe : ', type(Data_Integer))
print('Data Float : ', Data_Float, ' , Tipe : ', type(Data_Float))