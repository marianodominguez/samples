
grid = [["G","", "R","R", "", "" ,"","R" ], 
       ["G" ,"",  "","R", "", "" ,"","R" ],
       ["G","G", "R","R", "", "" ,"","R" ],
       ["G","" , "R","R", "R","" ,"R", "" ],
       ["" ,"" , "R","R", "", "" ,"", "" ],
       ["R","" , "R","R", "", "" ,"", "" ],
       ["R","" , "R","R", "", "" ,"", "" ]]


def neighbors(grid, p, color):
    result=[]
    
    xmax=len(grid)-1
    ymax=len(grid[xmax])-1
    
    for (x,y) in [(-1,0), (1,0), (0,-1), (0,1)]:
        cn = (p[0]+x, p[1]+y)
        if cn[0]>=0 and cn[1]>=0 and cn[0]<=xmax and cn[1]<=ymax:
            if grid[cn[0]][cn[1]] == color: result.append(cn)
    return result

def get_area(grid, point):
    color=grid[point[0]][point[1]]
    stack=[point]
    visited={}
    while stack:
        print(stack)
        current=stack.pop()
        visited[current] = 1
        for n in neighbors(grid, current, color):
            if not visited.get(n): stack.append(n)
            visited[current] = 1
    return visited.keys()

def count_area(grid, point):
  return len(get_area(grid, point))

print (get_area(grid,(2,3)))
print ("____")
print (get_area(grid,(0,7)))
print ("____")
print (get_area(grid,(2,1)))
print ("____")
print (get_area(grid,(6,0)))