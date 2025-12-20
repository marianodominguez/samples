'''
Quicksort implementation

reference: https://www.youtube.com/watch?v=SLauY6PpjW4

Time: O(n log n)
Space: O(log n)

'''

# Quicksort implementation
def qsort1(list):
    # Base case
    if len(list)==0:
        return []
    else:
        # Recursive case
        pivot = list[0]
        # Partition the list
        lesser = qsort1([x for x in list[1:] if x < pivot])
        greater = qsort1([x for x in list[1:] if x >= pivot])
        # Return the sorted list
        return lesser + [pivot] + greater

# Partition function
def partition(list,low,high):
    # Base case
    i=low-1
    # Pivot element
    pivot=list[high]
    print(list)
    for j in range(low,high):
        # If the current element is less than or equal to the pivot
        if list[j]<=pivot:
            i+=1
            # Swap elements
            list[i],list[j]=list[j],list[i]
    list[i+1],list[high]=list[high],list[i+1]
    # Return the pivot index
    return i+1

# Quicksort implementation recursive without comprehensions
def qsort(list,low,high):
    # Base case
    if len(list)==1:
        return list
    # Recursive case
    if low<high:
        pivot=partition(list,low,high)
        qsort(list,low,pivot-1)
        qsort(list, pivot+1,high)

# Test
list=[45, 9, 7, 5, 3, 2, 13, 10, 13, 4, 1, 6, 11]
n=len(list)
qsort(list,0,n-1)
print(list)
