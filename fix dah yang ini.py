import numpy as np 
from sympy import Matrix
import datetime
print("="*30, "HILL CIPHER", "="*28)
print()
print("-"*71)
print("| Menu 1. Enkripsi Data\t\t\t| Menu 2. Deskripsi Data")
print("| Menu 3. History Enkripsi\t\t| Menu 4. History Deskripsi")
print("\t\t\t    0 Keluar")
print("-"*71)
print()

for i in range(5):
    pilihan = int(input(">>> Masukkan menu yang Anda pilih : "))

    if pilihan == 1:
        pesan1 = input("Plaintext: ").upper()
        pesan1 = pesan1.replace(" ", "")
        pesanVector = np.array([[0]* int(len(pesan1)/3) for i in range(3)])
        a = 0
        for i in range(3):
            pesanVector[i] = ord(pesan1[a]) % 65
            a += 1

        kunci = input("Key : ").upper()
        kunci = kunci.replace(" ", "")
        kunciMatrix = np.array([[0]* int(len(kunci)/3) for i in range(3)])
        b = 0
        for i in range(3):
            for j in range(int(len(kunci)/3)):
                kunciMatrix[i][j] = ord(kunci[b]) % 65
                b += 1
        enskripsi = kunciMatrix.dot(pesanVector)

        matrix_cipher = enskripsi % 26
        listmatrix = []
        for i in range(3):
            listmatrix.append(chr(matrix_cipher[i][0] + 65))
            x = "".join(listmatrix)
        print("[OUTPUT] Ciphertext : ",x)
        ticks1 = datetime.datetime.now()
    elif pilihan == 2:
        pesan2 = input("Plaintext: ").upper()
        pesan2 = pesan2.replace(" ", "")
        pesanVector = np.array([[0]* int(len(pesan2)/3) for i in range(3)])
        a = 0
        for i in range(3):
            pesanVector[i] = ord(pesan2[a]) % 65
            a += 1

        kunci = input("Key : ").upper()
        kunci = kunci.replace(" ", "")
        kunciMatrix = np.array([[0]* int(len(kunci)/3) for i in range(3)])
        b = 0
        for i in range(3):
            for j in range(int(len(kunci)/3)):
                kunciMatrix[i][j] = ord(kunci[b]) % 65
                b += 1

        inverse = Matrix(kunciMatrix).inv_mod(26)
        inverse = np.array(inverse)
        Enkripsi = inverse.dot(pesanVector)
    
        matrix_cipher = Enkripsi % 26
        listmatrix = []
        for i in range(3):
            listmatrix.append(chr(matrix_cipher[i][0]+ 65))
            y = "".join(listmatrix)
        print("[OUTPUT] Ciphertext:",y)
        ticks2 = datetime.datetime.now()
    elif pilihan == 3:
        print()
        print("Selamat Datang Di Menu History")
        print("Anda mengakses Program Enkripsi pada: ")
        print("+---------------"+"+------------------"+"+----------------"+"+------------"+"+----------------------------+")
        print("| KODE ENKRIPSI |     PLAINTEXT    |       KEY      | CIPHERTEXT |      TANGGAL & WAKTU       |")
        print("+---------------"+"+------------------"+"+----------------"+"+------------"+"+----------------------------+")
        print("|", "\t",pilihan , "\t|\t",   pesan1, "      |\t" , kunci , " |\t ", x , "\t |", ticks1, "|")
        print("+---------------"+"+------------------"+"+----------------"+"+------------"+"+----------------------------+")
    elif pilihan == 4:
        print()
        print("Selamat Datang Di Menu History")
        print("Anda mengakses Program Deskripsi pada: ")
        print()
        print("+----------------"+"+------------------"+"+----------------"+"+------------"+"+----------------------------+")
        print("| KODE DESKRIPSI |     PLAINTEXT    |       KEY      | CIPHERTEXT |      TANGGAL & WAKTU       |")
        print("+----------------"+"+------------------"+"+----------------"+"+------------"+"+----------------------------+")
        print("|", "\t",pilihan , "\t |\t",   pesan2, "       |\t" , kunci , "  |\t ", y , "\t  |", ticks2,"|")
        print("+----------------"+"+------------------"+"+----------------"+"+------------"+"+----------------------------+")
    elif pilihan == 0:
        print("Program selesai")
        break
print()