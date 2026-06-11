def pengerjaan_soal_11_9():
    print("="*60)
    print("LEMBAR KERJA: PENYELESAIAN GAUSS-SEIDEL (SOAL 11.9)")
    print("="*60 + "\n")
    
    # Inisialisasi awal
    c1, c2, c3 = 0.0, 0.0, 0.0
    eps_s = 5.0 # Batas toleransi error dalam persen
    iterasi = 0
    error = 100.0
    
    print(f"{'Iterasi':<10} | {'c1':<10} | {'c2':<10} | {'c3':<10} | {'Error (%)'}")
    print("-" * 60)
    
    while error > eps_s:
        c1_old, c2_old, c3_old = c1, c2, c3
        
        # Iterasi Gauss-Seidel
        c1 = (3800 + 3*c2 + c3) / 15
        c2 = (1200 + 3*c1 + 6*c3) / 18
        c3 = (2350 + 4*c1 + c2) / 12
        
        iterasi += 1
        
        # Hitung error relatif maksimum
        ea1 = abs((c1 - c1_old) / c1) * 100
        ea2 = abs((c2 - c2_old) / c2) * 100
        ea3 = abs((c3 - c3_old) / c3) * 100
        error = max(ea1, ea2, ea3)
        
        print(f"{iterasi:<10} | {c1:<10.4f} | {c2:<10.4f} | {c3:<10.4f} | {error:.2f}%")

    print("\n" + "="*60)
    print("HASIL AKHIR:")
    print(f"Konsentrasi c1 = {c1:.4f} g/m^3")
    print(f"Konsentrasi c2 = {c2:.4f} g/m^3")
    print(f"Konsentrasi c3 = {c3:.4f} g/m^3")
    print("="*60)

pengerjaan_soal_11_9()