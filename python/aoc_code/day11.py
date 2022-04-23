def read_data():
    result=[]
    f = open("dumbo_tst.txt","r")
    for line in f:
        row=[int(x) for x in line.strip()]
        result.append(row)
    return result

def flash(grid,i,j):
    nflashes=1
    n=len(grid[0])
    m=len(grid)
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if x+i<n and x+i>=0 and y+j<m and y+j>=0:
                if not (i==0 and y==0): 
                    grid[i+x][j+y]+=1
    grid[i][j]=0
    return nflashes

def step(grid):
    n=len(grid[0])
    m=len(grid)
    nflashes=0
    for i in range(m):
        for j in range(n):
            grid[i][j]+=1
            if grid[i][j] >9 : 
                nflashes+=flash(grid,i,j)
    return nflashes
        

grid = read_data()

nsteps=2
nflashes=0
for i in range(nsteps):
    nflashes+=step(grid)
    print(grid)
    print(nflashes)