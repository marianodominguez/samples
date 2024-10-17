def inverse(s):
    word = ""
    stack = []
    idx = 0
    for chr in s:
        stack.append(chr)
        if chr == " " or idx >= len(s) - 1:
            while stack:
                c = stack.pop()
                word += c
        print("[",word,"]")
        idx +=1
    return word

print(inverse("esto es una frase "))