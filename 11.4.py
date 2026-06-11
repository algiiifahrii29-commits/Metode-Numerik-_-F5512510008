import numpy as np

def pengerjaan_soal_11_4():
    # Matriks yang diberikan berdasarkan konteks Contoh 11.2 (Sistem simetris)
    # A = L * L_transpose
    L = np.array([[2, 0, 0],
                  [-1, 1, 0],
                  [0, -1, 1]])
    
    # Target matriks A (asumsi dari contoh buku)
    A_target = np.array([[4, -2, 0],
                         [-2, 2, -1],
                         [0, -1, 2]])

    print("="*60)
    print("LEMBAR KERJA: KONFIRMASI CHOLESKY DECOMPOSITION (SOAL 11.4)")
    print("="*60 + "\n")
    
    print("Langkah 1: Identifikasi Matriks Segitiga Bawah [L]")
    print(f"Matriks [L] =\n{L}\n")
    
    print("Langkah 2: Menentukan Matriks Transpose [L]^T")
    L_T = L.T
    print(f"Matriks [L]^T =\n{L_T}\n")
    
    print("Langkah 3: Melakukan Perkalian [L] * [L]^T")
    A_hasil = np.dot(L, L_T)
    print("Perhitungan:")
    print(f"[{L}] * [{L_T}] =")
    print(f"{A_hasil}\n")
    
    print("Langkah 4: Kesimpulan")
    if np.array_equal(A_hasil, A_target):
        print("Hasil perkalian [L][L]^T identik dengan matriks [A] asal.")
        print("STATUS: Cholesky Decomposition terkonfirmasi valid.")
    else:
        print("Terdapat ketidaksesuaian antara hasil perkalian dengan matriks [A].")
    print("="*60)

# Jalankan simulasi
if __name__ == "__main__":
    pengerjaan_soal_11_4()