def read_data():
    result=[]
    f = open("chitons_tst.txt","r")
    for line in f:
        row=[ int(c) for c in line.strip() ]
        result.append(row)
    return result

def add_neighbors(p,stack,n,m, visited):
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if x!=0 or y!=0:
                nx=p[0]+x
                ny=p[1]+y
                if nx>=0 and nx<n and ny>=0 and ny<m:
                    if (nx,ny) and not visited[(nx,ny)]: stack.append( (nx,ny) )


def get_path(start, end, cave, path, visited):
    stack=[start]
    path=[]
    result=[]
    while stack:
        current=stack.pop()
        visited[current]=True
        if current==end:
            path.append(current)
            result.append(path)
            path=[]
            stack.append((0,0))
            visited[(0,0)]=False
            visited[end]=False
        else:
            add_neighbors(current,stack, n, m, visited)
            path.append(current)
    return result

cave=read_data()
print(cave)
start=(0,0)
m=len(cave)
n=len(cave[0])
end=(n-1,m-1)
path=[]
visited={(i,j):False for i in range(m) for j in range(n) }

print(get_path(start, end, cave,path, visited))

