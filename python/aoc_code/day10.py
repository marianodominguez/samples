from gettext import find


def read_data():
    result=[]
    f = open("nav_code_tst.txt","r")
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

d = read_data()
incomplete=[]
for line in d:
    if not find_corrupted(line):
        incomplete.append(line)

print(incomplete)