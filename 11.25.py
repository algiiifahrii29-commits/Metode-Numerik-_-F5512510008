"""Tugas Metode Numerik_Bapak Andi Hendra"""
"""Muhamad Algifahri_F5512510008"""


import numpy as np

def cholesky_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i + 1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                L[i][j] = np.sqrt(A[i][i] - s)
            else:
                L[i][j] = (1.0 / L[j][j] * (A[i][j] - s))
    return L

def solve_cholesky(A, b):
    L = cholesky_decomposition(A)
    # Langkah 1: Selesaikan Ly = b (substitusi maju)
    y = np.linalg.solve(L, b)
    # Langkah 2: Selesaikan L^T x = y (substitusi mundur)
    x = np.linalg.solve(L.T, y)
    return L, x

# Data Uji (Contoh matriks simetris dari Example 11.2)
A = np.array([[6, 15, 55],
              [15, 55, 225],
              [55, 225, 979]], dtype=float)
b = np.array([1, 6, -1], dtype=float)

L, x = solve_cholesky(A, b)

print("LEMBAR KERJA: DEKOMPOSISI CHOLESKY (SOAL 11.25)")
print("================================================")
print("Matriks L (Segitiga Bawah):\n", np.round(L, 4))
print("\nSolusi {x}:", np.round(x, 4))