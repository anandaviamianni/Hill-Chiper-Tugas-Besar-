import numpy as np 
from sympy import Matrix
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

enkripsiMessage = inverse_key.dot(pesanVector)
print(enkripsiMessage)
