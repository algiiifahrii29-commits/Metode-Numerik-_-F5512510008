"""Tugas Metode Numerik_Bapak Andi Hendra"""
"""Muhamad Algifahri_F5512510008"""


import numpy as np

def check_convergence(A, name):
    print(f"--- Uji {name} ---")
    n = A.shape[0]
    for i in range(n):
        diag = abs(A[i, i])
        off_diag = sum(abs(A[i, j]) for j in range(n) if i != j)
        print(f"Baris {i+1}: Diagonal {diag}, Jumlah off-diag {off_diag}")
        if diag <= off_diag:
            print("  -> Tidak memenuhi syarat dominan diagonal (Berpotensi Divergen)")

# Mendefinisikan Matriks
sets = {
    "Set One": np.array([[8, 3, 1], [-6, 0, 7], [2, 4, -1]]),
    "Set Two": np.array([[1, 1, 5], [1, 4, -1], [3, 1, -1]]),
    "Set Three": np.array([[-1, 3, 5], [-2, 4, -5], [0, 2, -1]])
}

for name, A in sets.items():
    check_convergence(A, name)