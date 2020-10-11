import numpy as np
from sympy import Matrix
pesan = input("Plaintext: ").upper()
pesan = pesan.replace(" ", "")
kunci = input("Key: ").upper()
kunci = pesan.replace(" ", "")

class cipher():
    def __init__(self, pesan, kunci):
        self.pesan = pesan
        self.kunci = kunci

    def enskripsi(self):
        pesanVector = np.array([[0]* int(len(self.pesan)/3) for i in range(3)])

        a = 0
        for i in range(3):
            for j in range(int(len(self.pesan)/3)):
                pesanVector[i][j] = ord(self.pesan[a]) % 65
                a += 1
    
        kunciMatrix = np.array([[0]* int(len(self.kunci)/3) for i in range(3)])

        b = 0
        for i in range(3):
            for j in range(int(len(self.kunci)/3)):
                kunciMatrix[i][j] = ord(self.kunci[b]) % 65
                b += 1

        try:
            enskripsi = kunciMatrix.dot(pesanVector)
        except: 
            enskripsi = pesanVector.dot(kunciMatrix)

        chipherMatrix = enskripsi % 26
        chipherText = []
        for i in range(3):
            chipherText.append(chr(chipherMatrix[i][0] + 65))
        print("Ciphertext : ", "".join(chipherText))

    def deskripsi(self):
        pesanVector = np.array([[0]* int(len(self.pesan)/3) for i in range(3)])
        a = 0
        for i in range(3):
            for j in range(int(len(self.pesan)/3)):
                pesanVector[i][j] = ord(self.pesan[a]) % 65
                a += 1
    
        kunciMatrix = np.array([[0]* int(len(self.kunci)/3) for i in range(3)])
    
        b = 0
        for i in range(3):
            for j in range(int(len(self.kunci)/3)):
                kunciMatrix[i][j] = ord(self.kunci[b]) % 65
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
        print("Ciphertext:", "".join(chipherText))

    def cetak(self):
        pilihan = int(input("1. Encyption\n2. Decryption\nEnter the choice: "))
        if pilihan == 1:
            print("-"*3, "Encryption", "-"*3, self.enskripsi())
        elif pilihan == 2:
            print("-"*3, "Decryption", "-"*3, self.deskripsi())
        else:
            print("Invalid Choice")
data = cipher(pesan,kunci)
data.cetak()