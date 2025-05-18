# list examples

a = [ x for x in range(50)]

print ('***************** splice ******************')

print (a[0:10])

print (a[10:])
print (a[:10])

print (a[-10:])
print (a[:-10])

print ('***************** list comprehension ******************')

print (a)
print ([ x*x for x in a])
print ([ x*x*x for x in a if x<10 ])
print ([ x for x in a if x%2 == 1])
print (list(filter(lambda x : x%2 ==1, a)))
