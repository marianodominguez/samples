def read_data():
    result=[]
    f = open("dumbo_tst.txt","r")
    for line in f:
        row=[int(x) for x in line.strip()]
        result.append(row)
    return result

def flash(grid,i,j):
    n=len(grid[0])
    m=len(grid)
    stack=[(i,j)]
    visited=[]
    while stack:
        #print(stack)
        current=stack.pop()
        if current not in visited: 
            visited.append(current)
        i=current[0]
        j=current[1]
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if x+i<n and x+i>=0 and y+j<m and y+j>=0:
                    if not (i==0 and y==0): 
                        grid[i+x][j+y]+=1
                        if grid[i+x][j+y]>9:
                            if (i+x,j+y) not in visited: 
                                stack.append((i+x,j+y))
    return visited

def step(grid):
    n=len(grid[0])
    m=len(grid)
    flashes=[]
    for i in range(m):
        for j in range(n):
            grid[i][j]+=1
    for i in range(m):
        for j in range(n):
            if grid[i][j] >9 and (i,j) not in flashes: 
                f = flash(grid,i,j)
                flashes.extend(f)
                print(flashes)
    for v in flashes: 
        if grid[v[0]][v[1]]>9:
            grid[v[0]][v[1]]=0
    return len(set(flashes))
        

grid = read_data()

nsteps=2
nflashes=0
for i in range(nsteps):
    nflashes+=step(grid)
    print(grid)
    print(nflashes)