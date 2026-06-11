"""Tugas Metode Numerik_Bapak Andi Hendra"""
"""Muhamad Algifahri_F5512510008"""



import numpy as np

def pengerjaan_soal_11_5():
    # Matriks A dan Vektor b
    A = np.array([[6., 15., 55.],
                  [15., 55., 225.],
                  [55., 225., 979.]])
    b = np.array([152.6, 585.6, 2488.8])

    print("="*65)
    print("LEMBAR KERJA: CHOLESKY DECOMPOSITION & SOLVER (SOAL 11.5)")
    print("="*65 + "\n")

    print("Langkah 1: Dekomposisi Cholesky [A] = [L][L]^T")
    # Menggunakan cholesky dari scipy
    L = np.linalg.cholesky(A)
    print(f"Matriks [L] (Segitiga Bawah):\n{np.round(L, 4)}\n")
    print(f"Matriks [L]^T (Transpose):\n{np.round(L.T, 4)}\n")

    print("Langkah 2: Substitusi Maju [L]{y} = {b}")
    y = np.linalg.solve(L, b)
    print(f"Hasil {y} = {np.round(y, 4)}\n")

    print("Langkah 3: Substitusi Mundur [L]^T{a} = {y}")
    a = np.linalg.solve(L.T, y)
    print(f"Hasil {a} = {np.round(a, 4)}\n")

    print("Langkah 4: Kesimpulan")
    print("-" * 40)
    print(f"Nilai a0 = {a[0]:.4f}")
    print(f"Nilai a1 = {a[1]:.4f}")
    print(f"Nilai a2 = {a[2]:.4f}")
    print("-" * 40)
    print("Status: Sistem Persamaan Linear telah diselesaikan.")
    print("="*65)

if __name__ == "__main__":
    pengerjaan_soal_11_5()


