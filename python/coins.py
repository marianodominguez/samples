'''
[] [1] [] []
[] [1,1] [2] []
[] [[1,1,1][2,1]] [] [3]
[] [[1,1,1,1],[2,1,1]] [2,2] [3,1]

'''

from collections import deque

def get_minimum_coins_dfs(denominations, n):
    result=[]
    queue=deque()
    visited=set()
    visited.add(0)
    new_amount=0
    current_amount=0
    denominations=sorted(denominations)
    queue.append((0,[]))
    while queue:
        current=queue.popleft()
        current_amount+=current[0]
        if current_amount==n:
            result.append(current[1])
            return result
        for d in denominations:
            new_amount=current_amount+d
            if new_amount not in visited:
                if new_amount<=n:
                    visited.add(new_amount)
                    new_combination=current[1].copy()
                    new_combination.append(d)
                    queue.append((new_amount,new_combination))
    return result

def get_minimum_coins_dp(denominations, n):
        result=[]
        denominations=sorted(denominations)
        m=len(denominations)
        solutions=[ [ [] for y in range(m) ] for x in range(n+1) ]
        
        for i in range(1,n+1):
            for j in range(m):
                if denominations[j]==i: solutions[i][j].append([i])
                if denominations[j]<i:
                    prev=i-denominations[j]
                    for k in range(len(solutions[prev])):
                        for s in solutions[prev][k]:
                            ns=s.copy()
                            ns.append(denominations[j])
                            ns=sorted(ns)
                            if ns not in solutions[i][j]: 
                                solutions[i][j].append(ns)
                if denominations[j]>i:
                    j=m
        for solution in solutions[n]:
            for s in solution:
                if s not in result: result.append(s)
        #print([len(x) for x in result])
        return result[-1] if len(result)>0 else []

    
print(get_minimum_coins_dfs([1,2,3],4))
#print(get_minimum_coins_dp([1,3,5,8],10))
#print(get_minimum_coins_dp([2,9,7],100))
#print(get_minimum_coins_dp([7,4,11],10))