'''
Find the area of a grid using a stack
The grid is a list of lists of characters
'''

# Grid
grid = [["G","", "R","R", "", "" ,"","R" ], 
       ["G" ,"",  "","R", "", "" ,"","R" ],
       ["G","G", "R","R", "", "" ,"","R" ],
       ["G","" , "R","R", "R","" ,"R", "" ],
       ["" ,"" , "R","R", "", "" ,"", "" ],
       ["R","" , "R","R", "", "" ,"", "" ],
       ["R","" , "R","R", "", "" ,"", "" ]]

# Get the neighbors of a point
def neighbors(grid, p, color):
    result=[]
    # Get the maximum x and y
    xmax=len(grid)-1
    ymax=len(grid[xmax])-1
    # Get the neighbors
    for (x,y) in [(-1,0), (1,0), (0,-1), (0,1)]:
        cn = (p[0]+x, p[1]+y)
        if cn[0]>=0 and cn[1]>=0 and cn[0]<=xmax and cn[1]<=ymax:
            if grid[cn[0]][cn[1]] == color: result.append(cn)
    return result

def get_area(grid, point):
    # Get the color of the point
    color=grid[point[0]][point[1]]
    # Initialize the stack
    stack=[point]
    # Initialize the visited dictionary
    visited={}
    # While there are points in the stack
    while stack:
        print(stack)
        current=stack.pop()
        # Mark the point as visited
        visited[current] = 1
        # Get the neighbors
        for n in neighbors(grid, current, color):
            # If the neighbor is not visited, add it to the stack
            if not visited.get(n): stack.append(n)
            visited[current] = 1
    # Return the visited points
    return visited.keys()

# Count the area of a point
def count_area(grid, point):
    # Return the number of points in the area
    return len(get_area(grid, point))

# Print the area of a point
print (get_area(grid,(2,3)))
print ("____")
print (get_area(grid,(0,7)))
print ("____")
print (get_area(grid,(2,1)))
print ("____")
print (get_area(grid,(6,0)))