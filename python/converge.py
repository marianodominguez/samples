import math
y1=1.0
y2=1.0
for i in range(1000000):
    y1=math.cos(y1)
    y2=math.sin(y2)
    print(f"sin(x)={y2}\tcos(x)={y1}")