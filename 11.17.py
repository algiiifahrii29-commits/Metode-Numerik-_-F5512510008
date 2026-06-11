import numpy as np

def f(x, y):
    return 4 - y - 2*x**2

def g(x, y):
    return 8 - y**2 - 4*x

def jacobian(x, y):
    return np.array([[-4*x, -1],
                     [-4, -2*y]])

def solve_nonlinear(x0, y0, tol=1e-6, max_iter=50):
    x = np.array([x0, y0], dtype=float)
    for _ in range(max_iter):
        F = np.array([f(x[0], x[1]), g(x[0], x[1])])
        J = jacobian(x[0], x[1])
        delta = np.linalg.solve(J, F)
        x = x - delta
        if np.linalg.norm(delta) < tol:
            return x
    return None

# Uji dengan beberapa tebakan awal untuk menemukan dua solusi
guesses = [(0, 0), (2, 2), (-2, -2)]
solutions = set()

for g_init in guesses:
    sol = solve_nonlinear(g_init[0], g_init[1])
    if sol is not None:
        solutions.add(tuple(np.round(sol, 4)))

print("LEMBAR KERJA: SISTEM PERSAMAAN NONLINEAR (SOAL 11.17)")
print("======================================================")
print("Solusi yang ditemukan (x, y):")
for s in solutions:
    print(f"x = {s[0]}, y = {s[1]}")