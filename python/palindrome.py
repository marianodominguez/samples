'''
Palindrome conjecture

Given an input, try to construct the palindrome by adding the inverse

Lychrel numbers are those that do not stop

196 does not stop
295 neither
394
493
689

ex. with 341 341+143=484
'''
# Mirror a number
def mirror(n):
    num=n
    mirror=0
    while num>0:
        digit=num % 10
        mirror=mirror*10+digit
        num=num // 10
    return mirror

# Check if a number is a palindrome
def isPalindrome(n):
    if n != mirror(n):
        return False
    return True

def construct(n):
    # Construct a palindrome by adding the inverse
    return n + mirror(n)

# Maximum number of iterations
MAX_ITER = 10000

def calculate(n):
    # Calculate the palindrome
    iter = 0
    x = n
    while not isPalindrome(x):
        x = construct(x)
        iter += 1
        # If the number is not a palindrome, it is a Lychrel number
        if iter > MAX_ITER or n==196:
            print(iter,"(", n, ")= possible Lychrel")
            iter = -1
            break
    # Print the result
    if iter >= 100:
        print(iter,"(", n, ")=", iter, " x=", x)

# Calculate the palindrome in parallel
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=100) as executor:
    for n in range(10, 100000):
        executor.submit(calculate, n)