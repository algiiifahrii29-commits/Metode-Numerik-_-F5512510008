import numpy as np

def pengerjaan_soal_11_8():
    # Parameter
    lambda_val = 1.2
    eps_s = 0.05 # 5%
    x = np.array([0.0, 0.0, 0.0]) # Tebakan awal
    
    print("="*60)
    print("LEMBAR KERJA: GAUSS-SEIDEL DENGAN OVER-RELAXATION")
    print("="*60 + "\n")
    
    iteration = 0
    error = 1.0
    
    while error > eps_s:
        iteration += 1
        x_old = np.copy(x)
        
        # Iterasi Gauss-Seidel dengan Over-Relaxation
        x[0] = (1 - lambda_val) * x[0] + lambda_val * ((41 + 0.4 * x[1]) / 0.8)
        x[1] = (1 - lambda_val) * x[1] + lambda_val * ((25 + 0.4 * x[0] + 0.4 * x[2]) / 0.8)
        x[2] = (1 - lambda_val) * x[2] + lambda_val * ((105 + 0.4 * x[1]) / 0.8)
        
        # Hitung error relatif
        error = np.max(np.abs((x - x_old) / x)) * 100
        print(f"Iterasi {iteration}: x1={x[0]:.4f}, x2={x[1]:.4f}, x3={x[2]:.4f} | Error: {error:.2f}%")
        
    print("\n" + "="*60)
    print("HASIL AKHIR:")
    print(f"x1 = {x[0]:.4f}")
    print(f"x2 = {x[1]:.4f}")
    print(f"x3 = {x[2]:.4f}")
    print("="*60)

if __name__ == "__main__":
    pengerjaan_soal_11_8()