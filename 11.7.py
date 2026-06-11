"""Tugas Metode Numerik_Bapak Andi Hendra"""
"""Muhamad Algifahri_F5512510008"""


import numpy as np

def pengerjaan_soal_11_7():
    # Definisi Matriks A
    A = np.array([[9., 0., 0.],
                  [0., 25., 0.],
                  [0., 0., 4.]])

    print("="*60)
    print("LEMBAR KERJA: DEKOMPOSISI CHOLESKY MATRIKS DIAGONAL (SOAL 11.7)")
    print("="*60 + "\n")

    print("Langkah 1: Identifikasi Matriks A")
    print(f"Matriks [A] =\n{A}\n")

    print("Langkah 2: Melakukan Dekomposisi Cholesky")
    # Menggunakan metode cholesky
    L = np.linalg.cholesky(A)
    
    print("Penjelasan:")
    print("Untuk matriks diagonal, elemen L_ii = sqrt(A_ii).")
    print(f"Hasil matriks [L] =\n{L}\n")

    print("Langkah 3: Verifikasi dengan [L][L]^T")
    A_verifikasi = np.dot(L, L.T)
    print(f"[L][L]^T =\n{A_verifikasi}\n")

    print("Langkah 4: Kesimpulan")
    if np.array_equal(A, A_verifikasi):
        print("Kesimpulan: Hasil dekomposisi terbukti benar dan konsisten.")
        print("Matriks [L] yang dihasilkan adalah matriks diagonal dengan akar dari elemen A.")
    print("="*60)

if __name__ == "__main__":
    pengerjaan_soal_11_7()