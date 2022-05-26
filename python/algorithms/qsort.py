#!/usr/bin/env python3

def qsort1(list):
    if len(list)==0:
        return []
    else:
        pivot = list[0]
        lesser = qsort1([x for x in list[1:] if x < pivot])
        greater = qsort1([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater

def partition(list,low,high):
    i=low-1
    pivot=list[high]
    print(list)
    for j in range(low,high):
        if list[j]<=pivot:
            i+=1
            list[i],list[j]=list[j],list[i]
    list[i+1],list[high]=list[high],list[i+1]
    return i+1

def qsort(list,low,high):
    if len(list)==1:
        return list
    if low<high:
        pivot=partition(list,low,high)
        qsort(list,low,pivot-1)
        qsort(list, pivot+1,high)

list=[45, 9, 7, 5, 3, 2, 13, 10, 13, 4, 1, 6, 11]
n=len(list)
qsort(list,0,n-1)
print(list)
