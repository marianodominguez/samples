'''
[] [1] [] []
[] [1,1] [2] []
[] [[1,1,1][2,1]] [] [3]
[] [[1,1,1,1],[2,1,1]] [2,2] [3,1]

'''


def count(S, m, n):
        result=[]
        solutions=[ [ [] for y in range(m) ] for x in range(n+1) ]
        
        for i in range(1,n+1):
            for j in range(m):
                if S[j]==i: solutions[i][j].append([i])
                if S[j]<i:
                    prev=i-S[j]
                    for k in range(len(solutions[prev])):
                        for s in solutions[prev][k]:
                            ns=s.copy()
                            ns.append(S[j])
                            ns=sorted(ns)
                            if ns not in solutions[i][j]: 
                                solutions[i][j].append(ns)
                if S[j]>i:
                    j=m
        for solution in solutions[n]:
            for s in solution:
                if s not in result: result.append(s)
        return result 

    
print(count([1,2,3],3,4))
print(count([1,3,5,8],4,10))