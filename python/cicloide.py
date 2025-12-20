'''
Cycloid curve

A cycloid is the curve traced by a point on the rim of a circular wheel as the wheel rolls along a straight line without slipping.
'''

import math
import matplotlib.pyplot as plt

# Number of points for a smooth curve
num_puntos = 1000

# Interval of the angle theta from 0 to 8π (4 turns)
theta = [t * (math.pi / 100) for t in range(num_puntos)]

# Radius of the circle
r=1

# Initialize the lists
x = []
y = []

# Calculate the x and y coordinates
for angulo in theta:
    # Calculate the x and y coordinates
    x_val = angulo - math.sin(angulo)
    y_val = 1 - math.cos(angulo)
    # Append the x and y coordinates to the lists
    x.append(r*(x_val))
    y.append(r*(y_val))

# Plot the curve
plt.plot(x, y, 'r')
# Title of the plot
plt.title('Cycloid curve')
# X label
plt.xlabel('X')
# Y label
plt.ylabel('Y')
# Grid
plt.grid(True)
# Show the plot
plt.show()