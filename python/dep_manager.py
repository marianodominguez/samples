def is_resolved(v, resolved):
    for item in v:
        if item not in resolved: return False
    return True

def build_order(dependencies):
    dep=dependencies.copy()
    result=[]
    resolved={}
    i=0
    while dep and i < len(dependencies):    
        for k,v in dep.items():
            if not v:
                if k not in resolved: 
                    result.append(k)
                    resolved[k]=True
            if is_resolved(v,resolved):
                if k not in resolved: 
                    result.append(k)
                    resolved[k]=True
                
        for item in result:
            if item in dep: dep.pop(item)
        i+=1
        
    if dep:
        print("unable to resolve")
        return []
    
    return result

print(build_order( {'File1':['File2', 'File3'], 'File2':['File3'], 'File3':[] } ))
print(build_order( {'File1':['File2'], 'File2':['File1'], 'File3':[] } ))
print(build_order( {'File1':['File2', 'File3'], 'File2':['File3'], 'File3':[], 'File4':[]  } ))
print(build_order( {'File1':['File3','File4' ], 'File2':['File4','File3'], 'File3':['File4'], 'File4':[]  } ))
