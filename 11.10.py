"""Tugas Metode Numerik_Bapak Andi Hendra"""
"""Muhamad Algifahri_F5512510008"""


def pengerjaan_soal_11_10():
    print("="*60)
    print("LEMBAR KERJA: PENYELESAIAN JACOBI ITERATION (SOAL 11.10)")
    print("="*60 + "\n")
    
    # Inisialisasi awal
    c1, c2, c3 = 0.0, 0.0, 0.0
    eps_s = 5.0 # Toleransi 5%
    iterasi = 0
    error = 100.0
    
    print(f"{'Iterasi':<10} | {'c1':<10} | {'c2':<10} | {'c3':<10} | {'Error (%)'}")
    print("-" * 60)
    
    while error > eps_s:
        c1_old, c2_old, c3_old = c1, c2, c3
        
        # Iterasi Jacobi (menggunakan nilai k untuk semua variabel)
        c1 = (3800 + 3*c2_old + c3_old) / 15
        c2 = (1200 + 3*c1_old + 6*c3_old) / 18
        c3 = (2350 + 4*c1_old + c2_old) / 12
        
        iterasi += 1
        
        # Hitung error relatif
        ea1 = abs((c1 - c1_old) / c1) * 100
        ea2 = abs((c2 - c2_old) / c2) * 100
        ea3 = abs((c3 - c3_old) / c3) * 100
        error = max(ea1, ea2, ea3)
        
        print(f"{iterasi:<10} | {c1:<10.4f} | {c2:<10.4f} | {c3:<10.4f} | {error:.2f}%")

    print("\n" + "="*60)
    print("HASIL AKHIR JACOBI:")
    print(f"c1 = {c1:.4f}, c2 = {c2:.4f}, c3 = {c3:.4f}")
    print("="*60)

pengerjaan_soal_11_10()