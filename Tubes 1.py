import numpy as np
from sympy import Matrix

def enskripsi():
    pesan = input("Plaintext: ")
    pesan.upper()
    pesan = pesan.replace(" ", "")
    pesanVector = np.array([[0]* int(len(pesan)/3) for i in range(3)])

    a = 0
    for i in range(3):
        for j in range(int(len(pesan)/3)):
            pesanVector[i][j] = ord(pesan[a]) % 65
            a += 1
    
    kunci = input("Key : ")
    kunci.upper()
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
    print("Ciphertext : ", "".join(chipherText))

def deskripsi():
    pesan = input("Plaintext: ")
    pesan.upper()
    pesan = pesan.replace(" ", "")

    pesanVector = np.array([[0]* int(len(pesan)/3) for i in range(3)])
    a = 0
    for i in range(3):
        for j in range(int(len(pesan)/3)):
            pesanVector[i][j] = ord(pesan[a]) % 65
            a += 1
    
    kunci = input("Key : ")
    kunci.upper()
    kunci = kunci.replace(" ", "")
    kunciMatrix = np.array([[0]* int(len(kunci)/3) for i in range(3)])
    
    b = 0
    for i in range(3):
        for j in range(int(len(kunci)/3)):
            kunciMatrix[i][j] = ord(kunci[b]) % 65
            b += 1

    inverse_key = Matrix(kunciMatrix).inv_mod(26)
    inverse_key = np.array(inverse_key)
    print(inverse_key)

    try:
        enkripsiMessage = inverse_key.dot(pesanVector)
    except:
        enkripsiMessage = pesanVector.dot(inverse_key)
    
    chipherMatrix = enkripsiMessage % 26
    chipherText = []
    for i in range(3):
        chipherText.append(chr(chipherMatrix[i][0]+ 65))
    print("Ciphertext:", "".join(chipherText))

def main():
    pilihan = int(input("1. Encyption\n2. Decryption\nEnter the choice: "))
    if pilihan == 1:
        print("-"*3, "Encryption", "-"*3)
        enskripsi()
    elif pilihan == 2:
        print("-"*3, "Decryption", "-"*3)
        deskripsi()
    else:
        print("Invalid Choice")

main()