import numpy as np 
pesan1 = input("Plaintext: ").upper()
pesan1 = pesan1.replace(" ", "")
pesanVector = np.array([[0]* int(len(pesan1)/3) for i in range(3)])
print(pesanVector)
print()

a = 0
for i in range(3):
    pesanVector[i] = ord(pesan1[a]) % 65
    a += 1
    print(pesanVector)
    print()

kunci = input("Key : ").upper()
kunci = kunci.replace(" ", "")
kunciMatrix = np.array([[0]* int(len(kunci)/3) for i in range(3)])
print(kunciMatrix)
print()

b = 0
for i in range(3):
    for j in range(int(len(kunci)/3)):
        kunciMatrix[i,j] = ord(kunci[b]) % 65
        b += 1
        print(kunciMatrix)
        print()

enskripsi = kunciMatrix.dot(pesanVector)
print(enskripsi)
print()
matrix_cipher = enskripsi % 26
print(matrix_cipher)
print()

listmatrix = []
for i in range(3):
    listmatrix.append(chr(matrix_cipher[i][0] + 65))
    print(listmatrix)
    x = "".join(listmatrix)
print("[OUTPUT] Ciphertext : ",x)