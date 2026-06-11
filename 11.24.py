"""Tugas Metode Numerik_Bapak Andi Hendra"""
"""Muhamad Algifahri_F5512510008"""


def thomas_algorithm(l, d, u, b):
    """
    Menyelesaikan sistem Ax = b untuk matriks tridiagonal
    l: diagonal bawah (panjang n-1)
    d: diagonal utama (panjang n)
    u: diagonal atas (panjang n-1)
    b: vektor hasil (panjang n)
    """
    n = len(d)
    # Forward elimination
    for i in range(1, n):
        w = l[i-1] / d[i-1]
        d[i] = d[i] - w * u[i-1]
        b[i] = b[i] - w * b[i-1]
        
    # Back substitution
    x = [0] * n
    x[n-1] = b[n-1] / d[n-1]
    for i in range(n-2, -1, -1):
        x[i] = (b[i] - u[i] * x[i+1]) / d[i]
        
    return x

# Uji coba dengan data Example 11.1
# Matriks tridiagonal contoh:
# d = [2.04, 2.04, 2.04, 2.04]
# l = [-1, -1, -1]
# u = [-1, -1, -1]
# b = [40.8, 0.8, 0.8, 200.8]

l = [-1.0, -1.0, -1.0]
d = [2.04, 2.04, 2.04, 2.04]
u = [-1.0, -1.0, -1.0]
b = [40.8, 0.8, 0.8, 200.8]

solusi = thomas_algorithm(l, d, u, b)

print("LEMBAR KERJA: ALGORITMA THOMAS (SOAL 11.24)")
print("============================================")
for i, val in enumerate(solusi):
    print(f"x[{i+1}] = {val:.4f}")