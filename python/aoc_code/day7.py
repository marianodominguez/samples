def read_data():
    f = open("whale.txt","r")
    return [int(s) for s in f.readline().rstrip().split(',')]

def iterate(pos):
    min_fuel=999999999999999
    for i in range (min(pos), max(pos)+1):
        dist = [abs(x-i) for x in pos ]
        d = sum (dist)
        if d<min_fuel:
            min_fuel=d
    return min_fuel

def triangular(n):
    if n==0 : return 0
    return n*(n+1)//2

def iterate_pt2(pos):
    min_fuel=999999999999999
    for i in range (min(pos), max(pos)+1):
        fuel = [triangular(abs(x-i)) for x in pos ]
        d = sum (fuel)
        #print(d,i)
        if d<min_fuel:
            min_fuel=d
    return min_fuel

def median_fuel(pos):
    median = sorted(pos)[len(pos)//2]
    return sum([abs(x-median) for x in pos])

pos=read_data()
min_fuel = iterate_pt2(pos)
print (min_fuel)