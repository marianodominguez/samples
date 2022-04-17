def isPalindrome(number):
    i=0
    len = n_digits(number)
    while i<len/2:
        if digit(number,i)!=digit(number, len-i-1):
            return False
        i+=1
    return True

def n_digits(number):
    n=0
    while number//pow(10,n)>0:
        n+=1
    return n

def digit(number, i):
    return int(number//pow(10,i)  - (number//pow(10, i+1))*10)

print(isPalindrome(33423423432))
print(isPalindrome(45345654354))