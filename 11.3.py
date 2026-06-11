"""Tugas Metode Numerik_Bapak Andi Hendra"""
"""Muhamad Algifahri_F5512510008"""


def pengerjaan_soal_11_3():
    print("="*60)
    print("LEMBAR KERJA: PENYELESAIAN SOAL 11.3 (ALGORITMA THOMAS)")
    print("="*60 + "\n")
    
    # Inisialisasi parameter
    f = [2.01475, 2.01475, 2.01475, 2.01475]
    e = [-0.020875, -0.020875, -0.020875]
    g = [-0.020875, -0.020875, -0.020875]
    r = [4.175, 0, 0, 2.0875]
    n = len(f)
    
    print("Langkah 1: Eliminasi Maju (Forward Elimination)")
    # Modifikasi g dan r
    g_prime = [0]*n
    r_prime = [0]*n
    
    g_prime[0] = g[0] / f[0]
    r_prime[0] = r[0] / f[0]
    
    for i in range(1, n):
        if i < n-1:
            g_prime[i] = g[i] / (f[i] - e[i-1] * g_prime[i-1])
        r_prime[i] = (r[i] - e[i-1] * r_prime[i-1]) / (f[i] - e[i-1] * g_prime[i-1])
        print(f"  -> Iterasi {i}: r_prime[{i}] = {r_prime[i]:.6f}")

    print("\nLangkah 2: Substitusi Mundur (Back Substitution)")
    T = [0]*n
    T[n-1] = r_prime[n-1]
    for i in range(n-2, -1, -1):
        T[i] = r_prime[i] - g_prime[i] * T[i+1]
        print(f"  -> T[{i+1}] = {T[i]:.6f}")
        
    print("\n" + "="*60)
    print("Hasil Akhir (Temperatur):")
    for i, val in enumerate(T):
        print(f"  T{i+1} = {val:.6f}")
    print("="*60)

pengerjaan_soal_11_3()
