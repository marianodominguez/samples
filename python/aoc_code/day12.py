def read_data():
    result={}
    f = open("caves_tst2.txt","r")
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

def get_paths(graph):
    stack=['start']
    visited={v:False for v in graph.keys() }
    result=[]
    path=[]
    while stack:
        current=stack.pop()
        path.append(current)
        if current=='end':
            result.append(path)
            path=[]
        if not visited[current] and not is_big(current):
            visited[current]=True
        for next in graph[current]:
            if not visited[next]:
                stack.append(next)
        visited['start']=False
    return result

graph=read_data()
print(graph)
print
print(get_paths(graph))

