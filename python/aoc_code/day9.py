from operator import mul
from functools import reduce

def read_data():
    result=[]
    f = open("lava.txt","r")
    for line in f:
        row=[int(d) for d in line.strip()]
        result.append(row)
    return result

def get_neighborgs(map, i, j ,n, m):
    result=[]
    if i+1<n : result.append(map[i+1][j])
    if i-1>=0 : result.append(map[i-1][j])
    if j+1<m : result.append(map[i][j+1])
    if j-1>=0 : result.append(map[i][j-1])
    return result

def get_next(map, i, j ,n, m):
    result=[]
    if i+1<n : result.append({'value':map[i+1][j], 'x': i+1, 'y':j})
    if i-1>=0 : result.append({'value':map[i-1][j], 'x': i-1, 'y':j})
    if j+1<m :  result.append({'value':map[i][j+1], 'x': i, 'y':j+1})
    if j-1>=0 : result.append({'value':map[i][j-1], 'x': i, 'y':j-1})
    return result

def low_points(map):
    result=[]
    n=len(map)
    m=len(map[0])
    for i in range(0,n):
        for j in range(0,m):
            neig= get_neighborgs(map,i,j,n,m)
            point= map[i][j]
            if list(filter( lambda x: x<=point, neig ) ) == []:
                result.append({'value': point, 'x': i, 'y': j })
    return result

def get_basin(point, map):
    n=len(map)
    m=len(map[0])
    result = []
    visited = []
    stack=[point]
    while stack:
        current = stack.pop()
        if current not in result : result.append(current)
        x=current['x']
        y=current['y']
        if (x,y) not in visited: visited.append((x,y))
        #print(result)
        next = get_next(map,x,y,n,m)
        for nx in next:
            if nx['value']<9 and (nx['x'],nx['y']) not in visited:
                stack.append(nx)
                #print(nx)
    return result


map = read_data()

low_points=low_points(map)
basins=[]
for p in low_points:
    basins.append( get_basin(p,map) )

by_size = sorted(basins, key=lambda x: len(x), reverse=True)

print(sum ( [ x['value']+1 for x in low_points ]) )
print(reduce(mul, [len(x) for x in by_size[0:3]],1)) 
