#!/usr/bin/env python3

# palindrome conjecture

# given an input, try to construct the palindrome by adding the inverse

# 196 does not stop
# 295 neither
# 394
# 493
# 689

# ex. with 341 341+143=484
def mirror(n):
    num=n
    mirror=0
    while num>0:
        digit=num % 10
        mirror=mirror*10+digit
        num=num // 10
    return mirror

def isPalindrome(n):
    if n != mirror(n):
        return False
    return True

def construct(n):
    return n + mirror(n)

MAX_ITER = 2000

for n in range(10, 100000):
    iter = 0
    x = n
    while not isPalindrome(x):
        x = construct(x)
        iter += 1
        if iter > MAX_ITER or n==196:
            print("iter(", n, ")= possible Lychrel")
            iter = -1
            break
    if iter >= 1:
        print("iter(", n, ")=", iter, " x=", x)
