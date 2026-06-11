import matplotlib.pyplot as plt
import numpy as np

def plot_gauss_seidel():
    # Persamaan: 
    # 1) -x + y = 2  (Slope 1)
    # 2) x + y = 4   (Slope -1)
    # Titik potong eksak: x=1, y=3
    
    x = np.linspace(0, 4, 100)
    y1 = x + 2
    y2 = -x + 4
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, label='y = x + 2 (Slope 1)')
    plt.plot(x, y2, label='y = -x + 4 (Slope -1)')
    
    # Simulasi Iterasi Gauss-Seidel
    x_val, y_val = 0, 0
    path_x, path_y = [x_val], [y_val]
    
    for i in range(5):
        # Update x dari pers 2: x = 4 - y
        x_val = 4 - y_val
        path_x.append(x_val); path_y.append(y_val)
        
        # Update y dari pers 1: y = x + 2
        y_val = x_val + 2
        path_x.append(x_val); path_y.append(y_val)
        
    plt.plot(path_x, path_y, 'ro--', label='Jalur Iterasi Gauss-Seidel')
    plt.scatter([1], [3], color='black', zorder=5) # Titik potong
    plt.legend(); plt.grid(True)
    plt.title("Iterasi Gauss-Seidel (Slope 1 dan -1)")
    plt.show()

plot_gauss_seidel()