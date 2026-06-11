


import numpy as np

# Definisi sistem
A = np.array([[10, 2, -1], [-3, -6, 2], [1, 1, 5]], dtype=float)
b = np.array([27, -61.5, -21.5], dtype=float)

# Inisialisasi awal (tebakan x = [0, 0, 0])
n = len(b)
x = np.zeros(n)
tol = 5.0  # Toleransi 5%
max_iter = 50

print("Iterasi Gauss-Seidel:")
for k in range(max_iter):
    x_old = x.copy()
    for i in range(n):
        s = sum(A[i][j] * x[j] for j in range(n) if i != j)
        x[i] = (b[i] - s) / A[i][i]
    
    # Menghitung error relatif persen untuk setiap variabel
    ea = np.max(np.abs((x - x_old) / x)) * 100
    
    print(f"Iterasi {k+1}: x1={x[0]:.4f}, x2={x[1]:.4f}, x3={x[2]:.4f}, Error={ea:.2f}%")
    
    if ea < tol:
        print(f"\nKonvergen pada iterasi ke-{k+1}")
        break