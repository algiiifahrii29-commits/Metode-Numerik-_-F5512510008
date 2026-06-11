"""Tugas Metode Numerik_Bapak Andi Hendra"""
"""Muhamad Algifahri_F5512510008"""


import numpy as np

# Misalkan A adalah matriks persegi n x n
n = 3
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Perintah satu baris untuk membuat matriks Aug [A|I]
Aug = np.hstack((A, np.eye(n)))

print("LEMBAR KERJA: MATRIKS AUGMENTASI (SOAL 11.21)")
print("==============================================")
print("Matriks A:\n", A)
print("\nMatriks Augmented [A|I]:\n", Aug)