'''
list comprehension examples

Time: O(n)
Space: O(n)

'''
# list from 0 to 50
a = [ x for x in range(50)]

print ('***************** splice ******************')
# first 10 elements
print (a[0:10])
# last 10 elements
print (a[10:])
# first 10 elements
print (a[:10])
# last 10 elements
print (a[-10:])
# first 10 elements
print (a[:-10])

print ('***************** list comprehension ******************')

print (a)
# square of each element
print ([ x*x for x in a])
# cube of each element if it is less than 10
print ([ x*x*x for x in a if x<10 ])
# list of odd elements
print ([ x for x in a if x%2 == 1])
# list of odd elements using filter
print (list(filter(lambda x : x%2 ==1, a)))
