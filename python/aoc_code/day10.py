from gettext import find

def read_data():
    result=[]
    f = open("nav_code.txt","r")
    for line in f:
        row=line.strip()
        result.append(row)
    return result

def find_corrupted(line):
    matches = { '(':')','{':'}','<':'>','[':']' }
    stack=[]
    #print(line)
    result=[]
    for ch in line:
        #print(ch)
        if ch in ['(','{','<','[']: 
            stack.append(ch)
            #print(stack)
        if ch in [')','}','>',']']: 
            if stack: 
                opening = stack.pop()
                if ch != matches[opening]:
                    result.append(ch)
    return result

def part1(d):
    cl=[]

    scores={ ')':3,'}':1197,'>':25137,']':57 }

    for line in d:
        cl.extend(find_corrupted(line))
    print(cl)
    print(sum( [scores[x] for x in cl] ))

def autocomplete(s):
    matches = { '(':')','{':'}','<':'>','[':']' }
    stack=[]
    result=[]
    for ch in line:
        if ch in ['(','{','<','[']: 
            stack.append(ch)
        if ch in [')','}','>',']']:
            stack.pop()
    while stack:
        i = stack.pop()
        result.append(matches[i])
    return result

def score(line):
    score = 0
    table=')]}>'
    for ch in line:
        score = score*5+table.find(ch)+1
    return score

d = read_data()
incomplete=[]
for line in d:
    if not find_corrupted(line):
        incomplete.append(line)
scores=[]
for line in incomplete:
    print(line)
    a =autocomplete(line)
    print("".join(a))
    scores.append(score(a))

mid = len(scores)//2
print(sorted(scores)[mid])