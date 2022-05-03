
def read_data():
    folds=[]
    coords=[]
    minx,miny,maxx,maxy=0,0,0,0
    f = open("paper.txt","r")
    for line in f:
        if line.startswith("fold"):
            #"fold along y=7"
            eq=line.find('=')
            sp=line.rfind(' ')            
            folds.append((line[sp:eq].strip(),int(line[eq+1:])))
        elif line.strip()!="":
            l = line.strip().split(',')
            c = (int(l[0]),int(l[1]))
            if c[0]>maxx: maxx=c[0]
            if c[1]>maxy: maxy=c[1]

            coords.append(c)
    return {"coords": coords, "folds": folds , 
        'minx': minx, 'maxx': maxx, 
        'miny': miny, 'maxy': maxy }

def set_grid(d):
    result=[]
    col = [ ' ' for y in range(d['maxx']+1)]
    for i in range(d['maxy']+1):
        result.append(col.copy())
    #print(result)
    for c in d['coords']:
        i=c[0]
        j=c[1]
        #print(c)
        result[j][i]='#'
    return result

def superpose(x,y):
    #print("merge :", x,y)
    return [" " if x[i]==" " and y[i]==" " else "#" for i in range(len(x))]

def fold_row(v1,v2):
    result = v2.copy()
    for i in range(len(v1)):
        if v1[-(i+1)]==' ' and v2[i]==' ':
            result[i]=' '
        else:
            result[i]='#'
    return result

def fold_paper(grid, fold):
    result=[]
    n=len(grid)
    m=len(grid[0])
    #print(fold)
    if fold[0]=='y':
        yf=fold[1]
        for y in range(yf):
            merge_row=2*yf-y
            if merge_row<n:
                result.append( superpose(grid[merge_row],grid[y]) )
            else:
                #print("copy: ", y)
                result.append(grid[y])
    if fold[0]=='x':
        xf=fold[1]
        for y in range(n):
            row = grid[y]
            result.append( fold_row(row[:xf],row[xf+1:]) )
    return result

def count(grid):
    result=0
    for row in grid:
        result+=row.count('#')
    return result

d = read_data()
#print(d)
grid = set_grid(d)

folds= d['folds']

for i in range(len(folds)):
    f=folds[i]
    grid=fold_paper(grid,f)
    
for row in grid:
    row.reverse()
    print("".join(row))



