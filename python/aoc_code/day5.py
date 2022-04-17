import re

def read_data():
    lines=[]
    f = open("thermal.txt","r")
    for line in f:
        val = re.split(',|\->', line.rstrip())
        lines.append( tuple([int(v) for v in val ]) )
    return lines


def print_map(map):
    for j in range(len(map)):
        print()
        for i in range(len(map[j])):
            e=map[i][j]
            print(str(e) if e>0 else ".",  end='')

vents=read_data()
map=[]
max_x=max([max(p[0],p[2]) for p in vents])
max_y=max([max(p[1],p[3]) for p in vents])
min_x=min([min(p[0],p[2]) for p in vents])
min_y=min([min(p[1],p[3]) for p in vents])

map=[ [0 for y in range(min_y, max_y+1)] for x in range(min_x,max_x+1) ]


for line in vents:
    x1=line[0]
    y1=line[1]
    x2=line[2]
    y2=line[3]
    sy=min(y1,y2)
    ey=max(y1,y2)
    sx=min(x1,x2)
    ex=max(x1,x2)
    #print(line)
    if x1==x2:
        for y in range(sy,ey+1):
            map[x1-min_x][y-min_y]+=1
    elif y1==y2:
        for x in range(sx, ex+1):
            map[x-min_x][y1-min_y]+=1
    else:
        if x1>x2:
            x2,x1=x1,x2
            y2,y1=y1,y2
        y=y1
        x=x1
        while x<=x2:
            map[x-min_x][y-min_y]+=1
            if y1<y2: 
                y+=1 
            else: 
                y-=1
            x+=1
total = 0

#print_map(map)

for row in map:
    total+=len( list(filter(lambda x: x>1, row)) )
print()
print(total)