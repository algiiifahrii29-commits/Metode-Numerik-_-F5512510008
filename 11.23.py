"""Tugas Metode Numerik_Bapak Andi Hendra"""
"""Muhamad Algifahri_F5512510008"""


import matplotlib.pyplot as plt
import numpy as np

# Rentang n
n_values = np.arange(2, 21)

# Fungsi menghitung jumlah operasi
# Gauss: (2/3)n^3 + n^2 - (2/3)n
def gauss_ops(n):
    return (2/3)*n**3 + n**2 - (2/3)*n

# Thomas: 8n - 7
def thomas_ops(n):
    return 8*n - 7

gauss_results = [gauss_ops(n) for n in n_values]
thomas_results = [thomas_ops(n) for n in n_values]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n_values, gauss_results, label='Eliminasi Gauss (O(n^3))', marker='o')
plt.plot(n_values, thomas_results, label='Algoritma Thomas (O(n))', marker='s')
plt.xlabel('Ukuran Matriks (n)')
plt.ylabel('Jumlah Operasi')
plt.title('Perbandingan Efisiensi: Eliminasi Gauss vs Algoritma Thomas')
plt.legend()
plt.grid(True)
plt.show()