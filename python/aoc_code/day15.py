from heapq import heappush,heappop

def read_data():
    result=[]
    f = open("chitons.txt","r")
    for line in f:
        row=[ int(c) for c in line.strip() ]
        result.append(row)
    return result

def expand_map(map):
    result=[]
    
    for maprow in map:
        nrow=[]
        for i in range(5):
            row=[ (x+i-1) % 9 +1 for x in maprow]   
            nrow.extend(row)
        result.append(nrow)
    n=len(result)
    for i in range(0,4):
        newrow=[]
        for j in range(n):
            newrow=[(x+i) % 9 +1  for x in result[j]]
            result.append(newrow)
    return result


def add_neighbors(p,queue,path,n,m, visited):
    for c in [(-1,0), (1,0), (0,-1), (0,1)]:
        x,y=c[0],c[1]
        nx=p[0]+x
        ny=p[1]+y
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if not visited[p]:
                newpath=list(path)
                newpath.append( (nx,ny) )
                risk = sum( [ cave[p[0]][p[1]] for p in newpath ]  )
                heappush( queue, (risk,newpath) )

def get_path(start, end, visited):
    queue=[]
    heappush(queue, (1, [start]) )
    path=[]
    while queue:
        print(".", end="")
        # get the path with min risk
        path=heappop(queue)[1]
        current = path[-1]
        if current==end:
            return path
        else:
            add_neighbors(current,queue,path, n, m, visited)
        visited[current]=True
    return path

cave=read_data()
cave=expand_map(cave)

i=0 
print(len(cave), len(cave[0]))
start=(0,0)
m=len(cave)
n=len(cave[0])
end=(n-1,m-1)
visited={(i,j):False for i in range(m) for j in range(n) }
path=get_path(start, end, visited)
print(path)
print( sum( [ cave[c[0]][c[1]] for c in path[1:]] ) )