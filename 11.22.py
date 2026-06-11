"""Tugas Metode Numerik_Bapak Andi Hendra"""
"""Muhamad Algifahri_F5512510008"""


import numpy as np

# Definisi Matriks Koefisien A dan Vektor b
A = np.array([[0, -7, 5],
              [0, 4, 7],
              [-4, 3, -7]])

b = np.array([50, -30, 40])

# 1. Mencari solusi x
x = np.linalg.solve(A, b)

# 2. Mencari Transpose Matriks A
A_transpose = A.T

# 3. Mencari Invers Matriks A
A_inv = np.linalg.inv(A)

print("LEMBAR KERJA: PENYELESAIAN SOAL 11.22")
print("========================================")
print("Matriks Koefisien A:\n", A)
print("\nSolusi {x}:", np.round(x, 4))
print("\nTranspose Matriks A:\n", A_transpose)
print("\nInvers Matriks A:\n", np.round(A_inv, 4))