import math
import matplotlib.pyplot as plt

# Número de puntos para una curva suave
num_puntos = 1000

# Intervalo del ángulo theta desde 0 hasta 8π (4 vueltas)
theta = [t * (math.pi / 100) for t in range(num_puntos)]

x = []
y = []
r=1

for angulo in theta:
    x_val = angulo - math.sin(angulo)
    y_val = 1 - math.cos(angulo)
    x.append(r*(x_val))
    y.append(r*(y_val))

plt.plot(x, y, 'r')
plt.title('Cicloide')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()