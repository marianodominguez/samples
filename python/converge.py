'''
Converge to a value

Calculate the cosine and sine of a value until it converges to a value

The cosine and sine of a value converge to a value 
'''
import math
# Initial values
y1=1.0
y2=1.0
# Iterate until the values converge
for i in range(1000000):
    y1=math.cos(y1)
    y2=math.sin(y2)
    # Print the values
    print(f"sin(x)={y2}\tcos(x)={y1}")