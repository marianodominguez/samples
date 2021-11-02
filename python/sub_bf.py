l = [ 1, -2, 3, 4, -5, 6 ]

def sub(l):
  maxsum=l[0]
  currsum=l[0]

  for i in range(len(l)):
    currsum = currsum + l[i]
    if currsum < 0:
      currsum = 0
    if maxsum < currsum:
      maxsum = currsum
  return maxsum


print sub(l)

