import numpy as np 
from sympy import Matrix

pesan2 = input("Plaintext: ").upper()
pesan2 = pesan2.replace(" ", "")
pesanVector = np.array([[0]* int(len(pesan2)/3) for i in range(3)])
print(pesanVector)
print()

a = 0
for i in range(3):
    pesanVector[i] = ord(pesan2[a]) % 65
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
        kunciMatrix[i][j] = ord(kunci[b]) % 65
        b += 1
print(kunciMatrix)
print()

inverse = Matrix(kunciMatrix).inv_mod(26)
print(inverse)
print()
inverse = np.array(inverse)
print(inverse)
print()
Enkripsi = inverse.dot(pesanVector)
print(Enkripsi)
print()

matrix_cipher = Enkripsi % 26
print(matrix_cipher)
print()

listmatrix = []
for i in range(3):
    listmatrix.append(chr(matrix_cipher[i][0]+ 65))
    print(listmatrix)
    y = "".join(listmatrix)
print("[OUTPUT] Ciphertext:",y)