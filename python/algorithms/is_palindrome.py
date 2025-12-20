'''

Find if a number is a palindrome without using string conversion

# Example
print(isPalindrome(33423423432))
print(isPalindrome(45345654354))

Time: O(n)
Space: O(1)
'''

# find if a number is a palindrome
def isPalindrome(number):
    i=0
    len = n_digits(number)
    # compare digits from the start and end until the middle
    while i<len/2:
        # if digits are not equal, return false
        if digit(number,i)!=digit(number, len-i-1):
            return False
        i+=1
    return True

# Count the number of digits
def n_digits(number):
    n=0
    while number//pow(10,n)>0:
        n+=1
    return n

# Get the i-th digit
def digit(number, i):
    return int(number//pow(10,i)  - (number//pow(10, i+1))*10)

# Test
print(isPalindrome(33423423432))
print(isPalindrome(45345654354))