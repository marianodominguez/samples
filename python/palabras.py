'''
Invert a string of words
'''
def inverse(s):
    word = ""
    # Use a stack to keep track of the words
    stack = []
    idx = 0
    # Invert the string
    for chr in s:
        stack.append(chr)
        # If the character is a space or the end of the string, pop the stack and add the word to the result
        if chr == " " or idx >= len(s) - 1:
            while stack:
                c = stack.pop()
                word += c
        # Print the word
        print("[",word,"]")
        idx +=1
    # Return the result
    return word

# Test the function
print(inverse("esto es una frase "))