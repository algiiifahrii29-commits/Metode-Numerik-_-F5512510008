import numpy as np

def pengerjaan_soal_11_6():
    A = np.array([[8., 20., 15.],
                  [20., 80., 50.],
                  [15., 50., 60.]])
    b = np.array([50., 250., 100.])

    print("="*60)
    print("LEMBAR KERJA: CHOLESKY DECOMPOSITION MANUAL (SOAL 11.6)")
    print("="*60 + "\n")

    print("Langkah 1: Dekomposisi Cholesky [A] = [L][L]^T")
    # Melakukan dekomposisi
    L = np.linalg.cholesky(A)
    print(f"Hasil dekomposisi matriks [L]:\n{np.round(L, 4)}\n")

    print("Langkah 2: Substitusi Maju [L]{y} = {b}")
    y = np.linalg.solve(L, b)
    print(f"Vektor {y} = {np.round(y, 4)}\n")

    print("Langkah 3: Substitusi Mundur [L]^T{x} = {y}")
    x = np.linalg.solve(L.T, y)
    print(f"Solusi {x} = {np.round(x, 4)}\n")

    print("Langkah 4: Kesimpulan Akhir")
    print("-" * 40)
    print(f"x1 = {x[0]:.4f}")
    print(f"x2 = {x[1]:.4f}")
    print(f"x3 = {x[2]:.4f}")
    print("-" * 40)
    print("="*60)

if __name__ == "__main__":
    pengerjaan_soal_11_6()