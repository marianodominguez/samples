#!/usr/bin/env python3

def qsort1(list):
    if len(list)==0:
        return []
    else:
        pivot = list[0]
        lesser = qsort1([x for x in list[1:] if x < pivot])
        greater = qsort1([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater

print(qsort1( [45, 9, 7, 5, 3, 2, 13, 10, 13, 4, 1, 6, 11] ))
