
def part1():
    f = open("sub_m.txt","r")
    n = []
    total_lines=0

    for line in f:
        bits=[ch for ch in line]
        if not n: n=[0 for i in range(len(line)-1)] 
        idx=0
        for bit in bits:
            if bit=="1": 
                n[idx]+=1
            idx+=1
        total_lines+=1
    print(n)

    gamma=['0' for i in range(len(n))]
    epsilon=['0' for i in range(len(n))]

    for i in range(len(n)):
        count=n[i]
        if count<total_lines/2:
            gamma[i]='0'
            epsilon[i]='1'
        else: 
            gamma[i]='1'
            epsilon[i]='0'
    print(gamma, epsilon)

    print( int("".join(gamma),2)*int("".join(epsilon),2))

def part2():
    f = open("sub_m.txt","r")
    m = [ line.rstrip() for line in f ]
    oxy=m.copy()
    idx=0
    while len(oxy)>1:
        ones=list(filter(lambda n: n[idx]=="1",oxy))
        zeroes=list(filter(lambda n: n[idx]=="0",oxy))
        oxy = ones if len(ones)>=len(zeroes) else zeroes
        idx+=1
    print(oxy)
    scrub=m.copy()
    idx=0
    while len(scrub)>1:
        ones=   list(filter(lambda n: n[idx]=="1",scrub))
        zeroes= list(filter(lambda n: n[idx]=="0",scrub))
        scrub = ones if len(ones)<len(zeroes) else zeroes
        idx+=1
    print(scrub)
    print(int(oxy[0],2)*int(scrub[0],2))
part2()