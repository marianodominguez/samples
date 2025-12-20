'''
Dependency manager example

Given a list of dependencies, return the order in which to build the files
'''

# Check if all dependencies are resolved
def is_resolved(v, resolved):
    for item in v:
        if item not in resolved: return False
    return True

# Build the order
def build_order(dependencies):
    # Copy the dependencies
    dep=dependencies.copy()
    # Result list
    result=[]
    # Resolved dictionary
    resolved={}
    i=0
    # While there are dependencies
    while dep and i < len(dependencies):    
        # For each dependency
        for k,v in dep.items():
            # If there are no dependencies
            if not v:
                if k not in resolved: 
                    result.append(k)
                    resolved[k]=True
            # If all dependencies are resolved
            if is_resolved(v,resolved):
                # Add the dependency to the result
                if k not in resolved: 
                    result.append(k)
                    resolved[k]=True
                
        # Remove the dependency from the dependencies
        for item in result:
            if item in dep: dep.pop(item)
        i+=1
        
    # If there are dependencies left, return an empty list
    if dep:
        print("unable to resolve")
        return []
    # Return the result
    return result

# Test the function
print(build_order( {'File1':['File2', 'File3'], 'File2':['File3'], 'File3':[] } ))
print(build_order( {'File1':['File2'], 'File2':['File1'], 'File3':[] } ))
print(build_order( {'File1':['File2', 'File3'], 'File2':['File3'], 'File3':[], 'File4':[]  } ))
print(build_order( {'File1':['File3','File4' ], 'File2':['File4','File3'], 'File3':['File4'], 'File4':[]  } ))
