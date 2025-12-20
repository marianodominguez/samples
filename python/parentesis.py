'''
Check if a string of parentheses is balanced

A string of parentheses is balanced if each opening parenthesis has a corresponding closing parenthesis.
'''
def is_balanced(s):
    # Use a stack to keep track of the opening parentheses
    stack = Stack()
    # Handle empty string
    if s == "":
        return True
    for chr in s:
        # Push opening parentheses
        if chr == "(":
            stack.push(chr)
        # Pop closing parentheses
        if chr == ")":
            if stack.isEmpty():
                return False
            else:
                stack.pop()
    # Return True if the stack is empty
    return stack.isEmpty()

# Test the function
assert not is_balanced("(((((")
assert is_balanced("() ()")
assert is_balanced("() (x) (( () (abc) cde ))")
assert not is_balanced("))))((((")
