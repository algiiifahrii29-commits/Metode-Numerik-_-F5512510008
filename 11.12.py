"""Tugas Metode Numerik_Bapak Andi Hendra"""
"""Muhamad Algifahri_F5512510008"""


import numpy as np

def gauss_seidel(A, b, x, lam, tol=0.05, max_iter=100):
    n = len(b)
    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x_new = (b[i] - s) / A[i][i]
            x[i] = (1 - lam) * x[i] + lam * x_new
        
        # Hitung eror relatif
        if np.linalg.norm(x) != 0:
            ea = np.max(np.abs((x - x_old) / x)) * 100
            if ea < tol:
                return x, k + 1
    return x, max_iter

# Matriks yang sudah disusun ulang agar dominan diagonal
A = np.array([[6, -1, -1], [6, 9, 1], [-3, 1, 12]], dtype=float)
b = np.array([3, 40, 50], dtype=float)

# (a) Tanpa Relaksasi (lambda = 1.0)
x_a, iter_a = gauss_seidel(A, b, np.zeros(3), lam=1.0)
# (b) Dengan Relaksasi (lambda = 0.95)
x_b, iter_b = gauss_seidel(A, b, np.zeros(3), lam=0.95)

print(f"(a) Tanpa Relaksasi: {np.round(x_a, 4)} (Iterasi: {iter_a})")
print(f"(b) Dengan Relaksasi: {np.round(x_b, 4)} (Iterasi: {iter_b})")