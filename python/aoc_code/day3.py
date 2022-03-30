

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
