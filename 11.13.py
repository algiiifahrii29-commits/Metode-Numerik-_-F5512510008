import numpy as np

def gauss_seidel(A, b, x, lam, tol=0.05, max_iter=100):
    n = len(b)
    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if i != j)
            # Rumus dengan relaxation factor (lambda)
            x_new = (b[i] - s) / A[i][i]
            x[i] = (1 - lam) * x[i] + lam * x_new
        
        # Cek error relatif (asumsi x_i tidak nol)
        ea = np.max(np.abs((x - x_old) / x)) * 100
        if ea < tol:
            return x, k + 1
    return x, max_iter

# Matriks setelah disusun ulang agar dominan diagonal
A = np.array([[8, -1, 2], [-2, 6, 1], [3, 1, -7]], dtype=float)
b = np.array([20, 38, 34], dtype=float)

# (a) Tanpa Relaksasi (lam = 1.0)
x_a, iter_a = gauss_seidel(A, b, np.zeros(3), lam=1.0)
# (b) Dengan Relaksasi (lam = 1.2)
x_b, iter_b = gauss_seidel(A, b, np.zeros(3), lam=1.2)

print(f"(a) Tanpa Relaksasi: {x_a} (Iterasi: {iter_a})")
print(f"(b) Dengan Relaksasi: {x_b} (Iterasi: {iter_b})")