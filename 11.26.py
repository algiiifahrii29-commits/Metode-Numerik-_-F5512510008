import numpy as np

def gauss_seidel(A, b, x_init, tol=1e-6, max_iter=100):
    n = len(b)
    x = x_init.astype(float)
    
    print(f"{'Iter':<10} | {'x1':<10} | {'x2':<10} | {'x3':<10}")
    print("-" * 45)
    
    for k in range(max_iter):
        x_old = x.copy()
        
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x[i] = (b[i] - s) / A[i][i]
            
        print(f"{k+1:<10} | {x[0]:<10.4f} | {x[1]:<10.4f} | {x[2]:<10.4f}")
        
        # Cek konvergensi
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            print(f"\nKonvergen pada iterasi ke-{k+1}")
            return x
            
    print("\nTidak konvergen setelah iterasi maksimum.")
    return x

# Contoh pengujian berdasarkan Example 11.3
# Sistem:
# 3x1 - 0.1x2 - 0.2x3 = 7.85
# 0.1x1 + 7x2 - 0.3x3 = -19.3
# 0.3x1 - 0.2x2 + 10x3 = 71.4

A = np.array([[3, -0.1, -0.2],
              [0.1, 7, -0.3],
              [0.3, -0.2, 10]])
b = np.array([7.85, -19.3, 71.4])
x_guess = np.zeros(3)

print("LEMBAR KERJA: METODE GAUSS-SEIDEL (SOAL 11.26)")
print("================================================")
solusi = gauss_seidel(A, b, x_guess)