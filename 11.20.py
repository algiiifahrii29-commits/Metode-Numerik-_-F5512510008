import numpy as np

# 1. Definisi input x
x = np.array([4, 2, 7, 10, 3, 5])
n = len(x)

# 2. Membuat matriks Vandermonde (6x6)
# increasing=True menghasilkan bentuk [1, x, x^2, ..., x^(n-1)]
A = np.vander(x, n, increasing=True)

# 3. Menghitung spectral condition number
cond_number = np.linalg.cond(A, p=2)

# 4. Membuat vektor b agar solusi eksak = [1, 1, 1, 1, 1, 1]
# b adalah jumlah dari setiap baris matriks A
b = np.sum(A, axis=1)

# 5. Menyelesaikan sistem persamaan
x_sol = np.linalg.solve(A, b)

print("LEMBAR KERJA: ANALISIS MATRIKS VANDERMONDE (SOAL 11.20)")
print("=======================================================")
print(f"Spectral Condition Number: {cond_number:.4e}")
print(f"Estimasi kehilangan digit presisi: {np.log10(cond_number):.2f} digit")
print(f"\nSolusi yang dihitung (seharusnya semua 1):")
print(np.round(x_sol, 4))
print(f"\nError relatif rata-rata: {np.mean(np.abs(x_sol - 1)):.2e}")