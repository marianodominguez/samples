
def boards():
    f = open("bingo.txt","r")
    draws=f.readline().rstrip()
    boards=[]
    idx=-1
    for line in f:
        if line=='\n':
            idx+=1
            boards.append([])
        else:
            bline=line.rstrip().split()
            boards[idx].append(bline)
    return draws,boards

print(boards())