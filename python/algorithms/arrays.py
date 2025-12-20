'''
Arrays algorithms

Find the 3rd biggest element in an array
Find the 2nd smallest element in an array
Find the 4th smallest element in an array
Invert a string
Invert a string without using a list
'''

# Find the 3rd biggest element in an array
from heapq import heappop,heappush

a = [-1,0,5,67,23,2,3,4,5,6]

#3rd biggest sorting
print( sorted(a)[-3] )
#2nd smallest sorting
print( sorted(a)[1] )
#not sorting 4th smallest
ac=a.copy()
#linear time k*n
for i in range(4):
    mini=min(ac)
    ac.remove(mini)
print(mini)

#using a heap
heap=[]
for e in a:
    heappush(heap,e)
for i in range(3):
     min=heappop(heap)   
print(min)

#invert string
a="inverting a string"
n=len(a)
al=[a[-i-1] for i in range(n)]
print("".join(al))

#invert string no list

a="inverting a string no list"
r=""
for c in a:
    r=c+r
print(r)


