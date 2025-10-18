import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# --- parámetros clásicos de Lorenz ---
sigma = 10.0
rho = 28.0
beta = 8.0/3.0

def lorenz(t, X):
    x,y,z = X
    return [sigma*(y-x), x*(rho - z) - y, x*y - beta*z]

# --- condiciones iniciales muy cercanas ---
x0 = np.array([1.0, 1.0, 1.0])
x0p = x0 + np.array([1e-8, 0.0, 0.0])   # perturbación pequeña

t_span = (0.0, 50.0)
t_eval = np.linspace(t_span[0], t_span[1], 5000)

sol1 = solve_ivp(lorenz, t_span, x0, t_eval=t_eval, rtol=1e-9, atol=1e-12)
sol2 = solve_ivp(lorenz, t_span, x0p, t_eval=t_eval, rtol=1e-9, atol=1e-12)

# Distancia en cada tiempo
dist = np.linalg.norm(sol1.y - sol2.y, axis=0)

plt.figure(figsize=(8,4))
plt.semilogy(t_eval, dist)
plt.xlabel('t')
plt.ylabel('distance ||x1-x2|| (log scale)')
plt.title('Divergencia entre dos condiciones iniciales cerca')
plt.grid(True)
plt.show()
