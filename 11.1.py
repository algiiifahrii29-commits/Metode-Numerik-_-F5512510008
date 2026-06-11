def pengerjaan_soal_11_1():
    print("LEMBAR JAWABAN TUGAS METODE NUMERIK")
    print("Nama: [Nama Anda]")
    print("Topik: Penyelesaian Sistem Persamaan Tridiagonal (Soal 11.1)")
    print("-" * 50)
    
    # Data soal
    diagonal = [0.8, 0.8, 0.8]
    sub_diag = [-0.4, -0.4]
    super_diag = [-0.4, -0.4]
    rhs = [41, 25, 105]
    
    print("Langkah 1: Identifikasi Matriks A dan Vektor b")
    print(f"Matriks A = [[{diagonal[0]}, {super_diag[0]}, 0],")
    print(f"             [{sub_diag[0]}, {diagonal[1]}, {super_diag[1]}],")
    print(f"             [0, {sub_diag[1]}, {diagonal[2]}]]")
    print(f"Vektor b = {rhs}\n")
    
    print("Langkah 2: Proses Eliminasi Maju (Thomas Algorithm)")
    # Simulasi manual langkah eliminasi
    # Eliminasi baris 2
    factor = sub_diag[0] / diagonal[0]
    new_diag_2 = diagonal[1] - (factor * super_diag[0])
    new_rhs_2 = rhs[1] - (factor * rhs[0])
    print(f"  -> Eliminasi x1 dari baris 2: diagonal baru menjadi {new_diag_2:.2f}")
    
    # Eliminasi baris 3
    factor2 = sub_diag[1] / new_diag_2
    new_diag_3 = diagonal[2] - (factor2 * super_diag[1])
    new_rhs_3 = rhs[2] - (factor2 * new_rhs_2)
    print(f"  -> Eliminasi x2 dari baris 3: diagonal baru menjadi {new_diag_3:.2f}")
    
    print("\nLangkah 3: Substitusi Mundur")
    # Hitung nilai x
    x3 = new_rhs_3 / new_diag_3
    x2 = (new_rhs_2 - super_diag[1] * x3) / new_diag_2
    x1 = (rhs[0] - super_diag[0] * x2) / diagonal[0]
    
    print(f"  -> x3 = {new_rhs_3:.2f} / {new_diag_3:.2f} = {x3:.2f}")
    print(f"  -> x2 = ({new_rhs_2:.2f} - ({super_diag[1]}) * {x3:.2f}) / {new_diag_2:.2f} = {x2:.2f}")
    print(f"  -> x1 = ({rhs[0]} - ({super_diag[0]}) * {x2:.2f}) / {diagonal[0]} = {x1:.2f}")
    
    print("-" * 50)
    print(f"Hasil Akhir: x1 = {x1:.2f}, x2 = {x2:.2f}, x3 = {x3:.2f}")

# Menjalankan fungsi
pengerjaan_soal_11_1()