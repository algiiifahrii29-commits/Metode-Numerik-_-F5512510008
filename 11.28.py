import numpy as np

def solve_pentadiagonal(A, r):
    n = len(r)
    # Membuat kopian agar A asli tidak berubah
    a = A.copy().astype(float)
    b = r.copy().astype(float)
    
    # 1. Forward Elimination (Eliminasi dua diagonal bawah)
    for i in range(n):
        # Eliminasi diagonal bawah ke-2 (jika ada)
        if i < n - 2:
            factor = a[i+2, i] / a[i, i]
            a[i+2, i:i+5] -= factor * a[i, i:i+5]
            b[i+2] -= factor * b[i]
            
        # Eliminasi diagonal bawah ke-1 (jika ada)
        if i < n - 1:
            factor = a[i+1, i] / a[i, i]
            a[i+1, i:i+5] -= factor * a[i, i:i+5]
            b[i+1] -= factor * b[i]
            
    # 2. Back Substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        sum_ax = sum(a[i, j] * x[j] for j in range(i+1, min(i+5, n)))
        x[i] = (b[i] - sum_ax) / a[i, i]
        
    return x

# Data Soal 11.28
A = np.array([[8, -2, -1, 0, 0],
              [-2, 9, -4, -1, 0],
              [-1, -3, 7, -1, -2],
              [0, -4, -2, 12, -5],
              [0, 0, -7, -3, 15]], dtype=float)
r = np.array([5, 2, 0, 1, 5], dtype=float)

solusi = solve_pentadiagonal(A, r)

print("LEMBAR KERJA: SISTEM PENTADIAGONAL (SOAL 11.28)")
print("================================================")
print("Hasil Solusi (x1 sampai x5):")
for i, val in enumerate(solusi):
    print(f"x{i+1} = {val:.4f}")