import numpy as np
import scipy.linalg as la

# Definisi matriks A
A = np.array([[0.8, -0.4, 0],
              [-0.4, 0.8, -0.4],
              [0, -0.4, 0.8]])

# 1. Melakukan LU Decomposition
# P adalah permutation matrix, L adalah lower triangular, U adalah upper triangular
P, L, U = la.lu(A)

print("LEMBAR KERJA: PENYELESAIAN SOAL 11.2 (LU DECOMPOSITION)")
print("="*60)
print("Matriks L (Lower):")
print(np.round(L, 3))
print("\nMatriks U (Upper):")
print(np.round(U, 3))

# 2. Menentukan Invers menggunakan LU Decomposition
# Kita menyelesaikan A * X = I, dimana I adalah matriks identitas
I = np.eye(3)
# Menggunakan solver yang memanfaatkan LU decomposition
A_inv = la.solve(A, I)

print("\nMatriks Invers [A]^-1:")
print(np.round(A_inv, 4))

# Verifikasi dengan A * A_inv
print("\nVerifikasi (A * A_inv harus mendekati Identitas):")
print(np.round(np.dot(A, A_inv), 3))