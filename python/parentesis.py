from stack import Stack

def is_balanced(s) :
    stack = Stack()
    if s == "" :
        return True
    for chr in s:
        if chr == "(" :
            stack.push(chr)
        if chr == ")" :
            if stack.isEmpty():
                return False
            else :
                stack.pop()
    return stack.isEmpty()
 
assert not is_balanced("(((((")
assert is_balanced("() ()") 
assert is_balanced("() (x) (( () (abc) cde ))")
assert not is_balanced("))))((((")

