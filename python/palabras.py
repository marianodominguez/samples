from stack import Stack

def inverse(s):
    word = ""
    stack = Stack()
    idx = 0
    for chr in s:
        stack.push(chr)
        if chr == " " or idx >= len(s) - 1:
            while not stack.isEmpty():
                c = stack.pop()
                word += c
        print "[",word,"]"
        idx +=1
    return word

print inverse("esto es una frase ")