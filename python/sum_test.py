import sys

def find_max_sum(a):
    sum_element=0
    max_so_far=0

    for e in a:
        sum_element+=int(e)
        if sum_element<0: sum_element=0
        if sum_element>max_so_far: max_so_far=sum_element
    return max_so_far

print(find_max_sum([10,8,-12,5,-9,100]))
print(find_max_sum([3,1,2,-1]))