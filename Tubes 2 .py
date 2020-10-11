import numpy as np
from sympy import Matrix
print("================================ Program Enkripsi ================================")
print('''
Ikutin ketentuan yang ada:
1.Input hanya terdiri dari 3 huruf kapital tanpa spasi
2.Bila diminta memasukan angka masukan angka yang ada dalam pilihan saja
3.Jika tidak mengikuti hal tersebut program akan error
''')
print('''
Program terdiri atas:
1.Enkripsi
2.deskripsi
Hanya pilih nomor
''')
try:
    inputan= int(input("Mana yang akan anda lakukan?[1/2]\n"))
    #siapin data2 yang dibutuhin
    a= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    key = "GYBNQKURP"
    #siapin list kosong
    d=[]    
    e=[]
    chiper_teks=[]
    ik=[]
    hasil_deskripsi=[]
    for i in key: #buat ngubah key jadi list yang berisi angka sesuai urutan abjab tersebut
        e.append(a.index(i))
    g= np.array(([e[0],e[1],e[2]],[e[3],e[4],e[5]],[e[6],e[7],e[8]])) #ngubah key jadi matriks

    if inputan ==1:
        print("Anda Sedang Melakukan Enkripsi")
        print()
        plain_teks =str(input("Masukan 3 Huruf Kapital yang akan di Enkripsi:\n"))
        print()
        key = str(input("Masukan Key:\n"))
        print()
        #ini buat enkripsi 
        print("Hasil enkripsi : ",end="")
        for i in plain_teks: #buat ngubah plain teks jadi list yang berisi angka sesuai urutan abjab tersebut
            d.append(a.index(i))

        for i in key: #buat ngubah key jadi list yang berisi angka sesuai urutan abjab tersebut
            e.append(a.index(i))

        f= np.array(([d[0]],[d[1]],[d[2]])) #ngubah plain text jadi matriks
        h= np.dot(g,f) #perkalian matriks plain text dengan key
        matriks_chiper= h%26 #buat nemuin matriks chiper teks
        
        for i in matriks_chiper : #masukin matriks chiper teks kedalam list
            for j in i:
                chiper_teks.append(a[j])

        for i in chiper_teks: #print output
            print(i,end="")
        print()
    
    elif inputan== 2:
        print("Anda Sedang Melakukan Deskripsi")
        print()
        plain_teks =str(input("Masukan 3 Huruf Kapital yang akan di Deskripsi:\n"))
        print()
        key = str(input("Masukan Key:\n"))
        print()
        invers_key = Matrix(g).inv_mod(26)
        for i in plain_teks: #buat ngubah plain teks jadi list yang berisi angka sesuai urutan abjab tersebut
            d.append(a.index(i))
        
        f= np.array(([d[0]],[d[1]],[d[2]])) #ngubah plain text jadi matriks
        inverse_key = np.array(invers_key)
        desk=np.dot(inverse_key,f) #perkalian matriks chiper dengan invers key
        deskripsi=desk%26 #hasil setelah di deskripsi
        
        #ini buat deskripsi
        print("Hasil Deskripsi: ",end="")
        for i in deskripsi : #masukin matriks chiper teks kedalam list
            for j in i:
                hasil_deskripsi.append(a[j])

        for i in hasil_deskripsi: #print output
            print(i,end="")
        print()
    else:
        print("Cuma ada 2 pilihan yaitu 1 atau 2")
        print("Program Error")
except :
    print("None")
    print("Ikuti perintah dengan teliti")
    print("Program Error")
finally:
    print("================================ Program Selesai================================")