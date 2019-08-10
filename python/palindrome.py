#!/usr/bin/env python2

# palindrome conjecture

# given an input, try to construct the palindrome by adding the inverse

# 196 does not stop
# 295 neither
# 394
# 493

# ex. with 341 341+143=484


def isPalindrome(n):
    digits = str(n)
    for i in xrange(len(digits)/2):
        digit = digits[i]
        mirror = digits[-(i+1)]
        if digit != mirror:
            return False
    return True


def construct(n):
    mirror = ''
    digits = str(n)
    mirror = digits[::-1]

    result = int(digits) + int(mirror)
    #print digits, "+", mirror, " = ", result
    return result

#inputString = input("give a number: ")
#n = int(inputString)


MAX_ITER = 20000

for n in xrange(1, 1000):
    iter = 0
    x = n
    while not isPalindrome(x):
        x = construct(x)
        iter += 1
        if iter > MAX_ITER:
            print "iter(", n, ")= unknown"
            iter = -1
            break
    if iter >= 1:
        print "iter(", n, ")=", iter, " x=", x
