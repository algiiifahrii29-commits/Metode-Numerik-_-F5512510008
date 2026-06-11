import numpy as np
import matplotlib.pyplot as plt

# Parameter
D, U, k, dx = 2, 1, 0.2, 2
x = np.arange(0, 12, dx) # 0, 2, 4, 6, 8, 10
n = len(x)
c0, c10 = 80, 20

# Membuat matriks A dan vektor b (untuk titik 2, 4, 6, 8)
n_inner = n - 2
A = np.zeros((n_inner, n_inner))
b = np.zeros(n_inner)

# Mengisi matriks
for i in range(n_inner):
    A[i, i] = -2.2
    if i > 0: A[i, i-1] = 0.75
    if i < n_inner - 1: A[i, i+1] = 0.25

# Syarat batas
b[0] -= 0.75 * c0
b[-1] -= 0.25 * c10

# Menyelesaikan sistem
c_inner = np.linalg.solve(A, b)
c = np.concatenate(([c0], c_inner, [c10]))

# Plotting
plt.plot(x, c, 'bo-')
plt.xlabel('Jarak (x)')
plt.ylabel('Konsentrasi (c)')
plt.title('Profil Konsentrasi di Sepanjang Kanal')
plt.grid(True)
plt.show()