import numpy as np
from scipy.linalg import hilbert

def solve_hilbert_19():
    n = 10
    # 1. Membuat matriks Hilbert 10x10
    H = hilbert(n)
    
    # 2. Menghitung spectral condition number (p=2)
    cond_num = np.linalg.cond(H, p=2)
    
    # 3. Estimasi kehilangan digit presisi
    lost_digits = np.log10(cond_num)
    
    # 4. Membuat vektor b agar solusi eksak adalah x = [1, 1, ..., 1]
    # Caranya: jumlahkan setiap elemen dalam baris matriks H
    b = np.sum(H, axis=1)
    
    # 5. Menyelesaikan sistem Hx = b
    x_sol = np.linalg.solve(H, b)
    
    # Menghitung eror (selisih terhadap solusi eksak 1)
    error = np.abs(x_sol - 1)
    
    print("LEMBAR KERJA: ANALISIS MATRIKS HILBERT (SOAL 11.19)")
    print("====================================================")
    print(f"Spectral Condition Number: {cond_num:.4e}")
    print(f"Estimasi digit yang hilang: {lost_digits:.2f} digit")
    print(f"\nError relatif rata-rata: {np.mean(error):.2e}")
    print("\nCatatan: Eror pada solusi jauh lebih besar dibandingkan jika matriks bersifat well-conditioned.")

solve_hilbert_19()