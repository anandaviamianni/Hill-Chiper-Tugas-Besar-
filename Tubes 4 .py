import numpy as np 
from sympy import Matrix
import datetime
print("="*20, "APLIKASI ENKRIPSI HILL CIPHER", "="*20)
print()
print("-"*71)
print("| Menu 1. Enkripsi Data\t\t\t| Menu 2. Deskripsi Data")
print("| Menu 3. History Enkripsi\t\t| Menu 4. History Deskripsi")
print("\t\t\t    [0] Keluar")
print("-"*71)
print()
pilihan = int(input(">>> Masukkan menu yang Anda pilih : "))
while pilihan != " ":
    if pilihan == 1:
        pesan = input("Plaintext: ").upper()
        pesan = pesan.replace(" ", "")
        pesanVector = np.array([[0]* int(len(pesan)/3) for i in range(3)])

        a = 0
        for i in range(3):
            for j in range(int(len(pesan)/3)):
                pesanVector[i][j] = ord(pesan[a]) % 65
                a += 1
        kunci = input("Key : ").upper()
        kunci = kunci.replace(" ", "")
        kunciMatrix = np.array([[0]* int(len(kunci)/3) for i in range(3)])

        b = 0
        for i in range(3):
            for j in range(int(len(kunci)/3)):
                kunciMatrix[i][j] = ord(kunci[b]) % 65
                b += 1

        try:
            enskripsi = kunciMatrix.dot(pesanVector)
        except: 
            enskripsi = pesanVector.dot(kunciMatrix)

        chipherMatrix = enskripsi % 26
        chipherText = []
        for i in range(3):
            chipherText.append(chr(chipherMatrix[i][0] + 65))
            x = "".join(chipherText)
        print("[OUTPUT] Ciphertext : ",x)
        ticks1 = datetime.datetime.now()
        pilihan = int(input(">>> Masukkan menu yang Anda pilih : "))
    elif pilihan == 2:
        pesan = input("Plaintext: ").upper()
        pesan = pesan.replace(" ", "")
        pesanVector = np.array([[0]* int(len(pesan)/3) for i in range(3)])
        a = 0
        for i in range(3):
            for j in range(int(len(pesan)/3)):
                pesanVector[i][j] = ord(pesan[a]) % 65
                a += 1

        kunci = input("Key : ").upper()
        kunci = kunci.replace(" ", "")
        kunciMatrix = np.array([[0]* int(len(kunci)/3) for i in range(3)])
        b = 0
        for i in range(3):
            for j in range(int(len(kunci)/3)):
                kunciMatrix[i][j] = ord(kunci[b]) % 65
                b += 1

        inverse_key = Matrix(kunciMatrix).inv_mod(26)
        inverse_key = np.array(inverse_key)

        try:
            enkripsiMessage = inverse_key.dot(pesanVector)
        except:
            enkripsiMessage = pesanVector.dot(inverse_key)
    
        chipherMatrix = enkripsiMessage % 26
        chipherText = []
        for i in range(3):
            chipherText.append(chr(chipherMatrix[i][0]+ 65))
            y = "".join(chipherText)
        print("Ciphertext:",y)
        ticks2 = datetime.datetime.now()
        pilihan = int(input(">>> Masukkan menu yang Anda pilih : "))
    elif pilihan == 3:
        print("+---------------"+"+------------------"+"+----------------"+"+------------"+"+----------------------------+")
        print("| KODE ENKRIPSI |     PLAINTEXT    |       KEY      | CIPHERTEXT |      TANGGAL & WAKTU       |")
        print("+---------------"+"+------------------"+"+----------------"+"+------------"+"+----------------------------+")
        print("|", "\t",pilihan , "\t|\t",   pesan, "      |\t" , kunci , " |\t ", x , "\t |", ticks1, "|")
        print("+---------------"+"+------------------"+"+----------------"+"+------------"+"+----------------------------+")
        pilihan = int(input(">>> Masukkan menu yang Anda pilih : "))
    elif pilihan == 4:
        print("+----------------"+"+------------------"+"+----------------"+"+------------"+"+----------------------------+")
        print("| KODE DESKRIPSI |     PLAINTEXT    |       KEY      | CIPHERTEXT |      TANGGAL & WAKTU       |")
        print("+----------------"+"+------------------"+"+----------------"+"+------------"+"+----------------------------+")
        print("|", "\t",pilihan , "\t |\t",   pesan, "       |\t" , kunci , "  |\t ", y , "\t  |", ticks2,"|")
        print("+----------------"+"+------------------"+"+----------------"+"+------------"+"+----------------------------+")
        pilihan = int(input(">>> Masukkan menu yang Anda pilih : "))
    elif pilihan == 0:
        print("Anda telah keluar dari Program")
print("Program Selesai")