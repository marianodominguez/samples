'''
FizzBuzz

Print the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number.
For multiples of five print "Buzz" instead of the number.
For numbers which are multiples of both three and five print "FizzBuzz".
'''

# Print the numbers from 1 to 100
for i in range(100):
    # Print "fizzbuzz" if the number is a multiple of 3 and 5
    if i % 3 ==0 and i % 5==0: 
        print("fizzbuzz")
    # Print "fizz" if the number is a multiple of 3
    elif i % 3 == 0: 
        print("fizz")
    # Print "buzz" if the number is a multiple of 5
    elif i % 5 ==0: 
        print("buzz")
    # Print the number
    else: 
        print(i) 