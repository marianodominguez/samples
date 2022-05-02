
def read_data():
    result={}
    f = open("caves.txt","r")
    for line in f:
        vertices = line.split("-")
        start=vertices[0].strip()
        end=vertices[1].rstrip()
        if start not in result.keys():
             result[start]=[end]
        else:
            result[start].append(end)
        if end not in result.keys():
             result[end]=[start]
        else:
            result[end].append(start)
    return result

def is_big(cave):
    return cave.upper()==cave

def is_small(cave):
    return cave.lower()==cave and cave not in ['start','end'] 

def getAllPaths(u,d,visited,path,result):
    if not is_big(u): 
        visited[u]=1
    path.append(u)

    if u==d:
        result.append(path.copy())
    else:
        for i in graph[u]:
            if not visited[i]:
                result=getAllPaths(i,d,visited,path,result)
    path.pop()
    visited[u]=0
    return result

def can_visit(i, visited, path):
    small_caves=set(filter( lambda x: is_small(x), path))
    if is_big(i): 
        return True
    if  i in ['start','end'] and visited[i]==0:
        return True
    # visit one small cave twice max
    if is_small(i) and visited[i]<1:
        return True
    visited_small=[ visited[c] for c in small_caves if visited[c]>=2]
    if is_small(i) and visited[i]==1 and len(visited_small)==0:
        return True
    return False

def getAllPathsP2(u,d,visited,path,result):
    visited[u]+=1
    path.append(u)

    if u==d:
        result.append(path.copy())
    else:
        for i in graph[u]:
            if can_visit(i, visited, path):
                result=getAllPathsP2(i,d,visited,path,result)
    path.pop()
    if visited[u]>0: 
        visited[u]-=1
    
    return result

def get_paths(graph):
    visited={v:0 for v in graph.keys() }
    result=[]
    path=[]
    result=getAllPathsP2("start", "end", visited, path, result)
    return result

graph=read_data()
print(graph)
p=get_paths(graph)
#print( "\n".join( sorted([",".join(r) for r in p]) ) )
print(len(p))

