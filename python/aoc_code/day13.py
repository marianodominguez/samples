
from json.encoder import INFINITY

def read_data():
    folds=[]
    coords=[]
    minx,miny,maxx,maxy=0,0,0,0
    f = open("paper_tst.txt","r")
    for line in f:
        if line.startswith("fold"):
            #"fold along y=7"
            eq=line.find('=')
            sp=line.rfind(' ')            
            folds.append((line[sp:eq].strip(),int(line[eq+1:])))
        elif line.strip()!="":
            l = line.strip().split(',')
            c = (int(l[0]),int(l[1]))
            if c[0]<minx: minx=c[0]
            if c[0]>maxx: maxx=c[0]
            if c[1]<miny: miny=c[1]
            if c[1]>maxy: maxy=c[1]

            coords.append(c)
    return {"coords": coords, "folds": folds , 
        'minx': minx, 'maxx': maxx, 
        'miny': miny, 'maxy': maxy }

def set_grid(d):
    result=[]
    col = [ ' ' for y in range(d['maxy']-d['miny']+1)]
    for i in range(d['maxx']-d['minx']+1):
        result.append(col)
    print(result)
    for c in d['coords']:
        x=c[0]
        y=c[1]
        print(c)
        result[x][y]='#'
    return result

def superpose(x,y):
    #print("merge :", x,y)
    return x

def fold_paper(grid, fold):
    result=[]
    n=len(grid)
    m=len(grid[0])
    print(fold)
    if fold[0]=='y':
        yf=fold[1]
        for y in range(yf):
            merge_row=2*yf-y
            if merge_row<n:
                print("merge: ",y, merge_row)
                result.append( superpose(grid[merge_row],grid[y]) )
            else:
                print("copy: ", y)
                result.append(grid[y])
    return result

d = read_data()
print(d)
grid = set_grid(d)

print(grid)

for f in d['folds']:
     grid=fold_paper(grid,f)


