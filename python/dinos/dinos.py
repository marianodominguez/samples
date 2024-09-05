'''
Given the following formula,

speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)

Where g = 9.8 m/s^2 (gravitational constant)

Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
'''
import math

dinos = {}
g = 9.8

f = open('dataset2.csv', "r")
for line in f:
    record = line.split(',')
    if record[2].strip() == 'bipedal':
        d = {
            "name":   record[0],
            "stride": float(record[1]),
            "speed": 0.0
            }
        dinos[record[0]] = d

#print(dinos)

f=open('dataset1.csv', "r")

for line in f:
    record = line.split(",")
    name = record[0].strip()
    if name in dinos:
        d = dinos[name]
        d["leg_len"] = float(record[1])
        d["speed"] = ((d["stride"] / d["leg_len"]) - 1) * math.sqrt(d["leg_len"] * g)

list_dinos=list(dinos.values())

list_dinos.sort(key=lambda d : d["speed"], reverse=True)

for d in list_dinos:
    print(d)