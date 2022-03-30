f = open("sub.txt")
x,d,aim=0,0,0
command=[]
for line in f:
    command=line.split(" ")
    if command[0]=="forward": 
        x += int(command[1]) 
        d += aim*int(command[1])
    if command[0]=="down": aim += int(command[1])
    if command[0]=="up": aim -= int(command[1])
print(x*d)