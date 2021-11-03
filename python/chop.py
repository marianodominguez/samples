def chop(elem, a):
  n=len(a)
  if n==0:
     return -1
  mid=n//2
  if elem==a[mid]:
     return mid
  if elem>a[mid]:
     return chop(elem, a[mid+1:n])
  else:
     return chop(elem, a[0:mid])

print(chop(2,[1,2,3]))

print(chop(3, []))
print(chop(3, [1]))
print(chop(1, [1]))
#
print(chop(1, [1, 3, 5]))
print(chop(3, [1, 3, 5]))
print(chop(5, [1, 3, 5]))
print(chop(0, [1, 3, 5]))
print(chop(2, [1, 3, 5]))
print(chop(4, [1, 3, 5]))
print(chop(6, [1, 3, 5]))
#
print(chop(1, [1, 3, 5, 7]))
print(chop(3, [1, 3, 5, 7]))
print(chop(5, [1, 3, 5, 7]))
print(chop(7, [1, 3, 5, 7]))

print(chop(0, [1, 3, 5, 7]))
print(chop(2, [1, 3, 5, 7]))
print(chop(4, [1, 3, 5, 7]))
print(chop(6, [1, 3, 5, 7]))
print(chop(8, [1, 3, 5, 7]))
