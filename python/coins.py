'''
Coin change problem

Given a list of coins and a target amount, return the minimum number of coins needed to make the target amount
Test 2 different algorithms: Breadth first search and Dynamic programming

Test cases:
[] [1] [] []
[] [1,1] [2] []
[] [[1,1,1][2,1]] [] [3]
[] [[1,1,1,1],[2,1,1]] [2,2] [3,1]

'''

from collections import deque

# Breadth first search
def get_minimum_coins_bfs(denominations, n):
    # Initialize the result
    result=[]
    # Initialize the queue
    queue=deque()
    # Initialize the visited set
    visited=set()
    visited.add(0)
    # Initialize the new amount
    new_amount=0
    # Initialize the current amount
    current_amount=0
    # Sort the denominations
    denominations=sorted(denominations)
    # Add the initial state to the queue
    queue.append((0,[]))
    # While there are items in the queue
    while queue:
        # Get the current item
        current=queue.popleft()
        # Get the current amount
        current_amount=current[0]
        # If the current amount is equal to the target amount, return the result
        if current_amount==n:
            result.append(current[1])
            return result[0]
        # For each denomination
        for d in denominations:
            # Calculate the new amount
            new_amount=current_amount+d
            # If the new amount is not in the visited set
            if new_amount not in visited:
                # If the new amount is less than or equal to the target amount
                visited.add(new_amount)
                # Add the new combination to the queue
                new_combination=current[1].copy()
                new_combination.append(d)
                queue.append((new_amount,new_combination))
    # Return the result
    return result[0] if len(result)>0 else []

# Dynamic programming
def get_minimum_coins_dp(denominations, n):
    # Initialize the result
    result=[]
    # Initialize the denominations
    denominations=sorted(denominations)
    m=len(denominations)
    # Initialize the solutions
    solutions=[ [ [] for y in range(m) ] for x in range(n+1) ]
    
    # For each amount
    for i in range(1,n+1):
        # For each denomination
        for j in range(m):
            # If the denomination is equal to the amount
            if denominations[j]==i: solutions[i][j].append([i])
            # If the denomination is less than the amount
            if denominations[j]<i:
                # Calculate the previous amount
                prev=i-denominations[j]
                # For each solution
                for k in range(len(solutions[prev])):
                    for s in solutions[prev][k]:
                        # Create a new solution
                        ns=s.copy()
                        ns.append(denominations[j])
                        ns=sorted(ns)
                        # Add the new solution to the solutions list
                        if ns not in solutions[i][j]: 
                            solutions[i][j].append(ns)
                # If the denomination is greater than the amount, break
                if denominations[j]>i: j=m
    # For each solution
    for solution in solutions[n]:
        for s in solution:
            if s not in result: result.append(s)
    # Return the result
    return result

# Test the function
print(get_minimum_coins_bfs([1,2,3],4))
print(get_minimum_coins_bfs([1,3,5,8],10))
print(get_minimum_coins_bfs([2,9,7],17))
print(get_minimum_coins_bfs([7,4,11],10))