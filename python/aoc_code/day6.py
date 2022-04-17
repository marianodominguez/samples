#!/usr/bin/python3 -u

def read_data():
    f = open("fish.txt","r")
    return [int(s) for s in f.readline().rstrip().split(',')]

def iterate_brute(pop, max_time):   
    t=0
    while t<max_time:
        n=len(pop)
        for i in range(n):
            if pop[i]>0: 
                pop[i]-=1
            else:
                pop.append(8)
                pop[i]=6
        t+=1
        print(t, len(pop))
    return len(pop)

def iterate(pop, max_time):
    pmap = {x:0 for x in range(0,9)}
    t=0
    for x in pop:
        pmap[x]+=1
    while t<max_time:
        new_fish = pmap[0]
        for i in range(1,9):
            pmap[i-1]=pmap[i]
        pmap[8]=new_fish
        pmap[6]+=new_fish
        t+=1
        print(pmap)
    return(sum([v for v in pmap.values() ]) )

max_time=256
pop=read_data()
npop = iterate(pop, max_time)
print( npop )
