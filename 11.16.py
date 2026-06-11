"""Tugas Metode Numerik_Bapak Andi Hendra"""
"""Muhamad Algifahri_F5512510008"""


import numpy as np

def analyze_matrix(A, b, label):
    # 1. Menghitung solusi
    x = np.linalg.solve(A, b)
    
    # 2. Menghitung invers
    A_inv = np.linalg.inv(A)
    
    # 3. Menghitung condition number (row-sum norm / infinity norm)
    cond_num = np.linalg.cond(A, np.inf)
    
    print(f"--- ANALISIS {label} ---")
    print(f"Solusi {x}")
    print(f"Condition Number (row-sum norm): {cond_num:.4e}")
    print(f"Invers Matriks:\n{np.round(A_inv, 2)}\n")

# Data Soal (a)
A_a = np.array([[1, 4, 9], [4, 9, 16], [9, 16, 25]], dtype=float)
b_a = np.array([14, 29, 50], dtype=float)

# Data Soal (b)
A_b = np.array([[1, 4, 9, 16], [4, 9, 16, 25], [9, 16, 25, 36], [16, 25, 36, 49]], dtype=float)
b_b = np.array([30, 54, 86, 126], dtype=float)

analyze_matrix(A_a, b_a, "Matriks (a)")
analyze_matrix(A_b, b_b, "Matriks (b)")