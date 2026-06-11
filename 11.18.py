"""Tugas Metode Numerik_Bapak Andi Hendra"""
"""Muhamad Algifahri_F5512510008"""


import numpy as np

# Definisi matriks koefisien A dan vektor hasil b
A = np.array([[4, 3, 2],
              [1, 3, 1],
              [2, 1, 3]])

b = np.array([960, 510, 610])

# Menyelesaikan sistem persamaan linear Ax = b
x = np.linalg.solve(A, b)

print("LEMBAR KERJA: PENYELESAIAN SOAL 11.18")
print("======================================")
print(f"Jumlah Transistor (x1)     : {x[0]:.0f}")
print(f"Jumlah Resistor (x2)       : {x[1]:.0f}")
print(f"Jumlah Chip Komputer (x3)  : {x[2]:.0f}")