
def read_boards():
    f = open("bingo_tst.txt","r")
    draws=[int(s) for s in f.readline().rstrip().split(',')]
    boards=[]
    idx=-1
    for line in f:
        if line=='\n':
            idx+=1
            boards.append([])
        else:
            bline=[int(s) for s in line.rstrip().split()]
            boards[idx].append(bline)
    return (draws,boards)

def winner(mark):
    n=len(mark[0])
    for row in mark:
        if sum(row)==n: return True
    for j in range(n):
        if sum([mark[i][j] for i in range(n)]) == n: return True
    return False

def play(boards,card,marks):
    for idx,board in enumerate(boards):
        for row in range(len(board)):
            for col in range(len(board[row])):
                e=board[row][col]
                if e==card:
                    marks[idx][row][col]=1
                if winner(marks[idx]): 
                    return (board,card,marks[idx])
    return ()


def bingo(draws,boards):
    marks=[]
    for b in boards:
        #print(b)
        #print("----")
        marks.append([ [0 for row in range(len(b[0])) ] for col in range(len(b)) ] )
    #print(marks[0])    
    card=0;
    winner=()
    while not winner:
        winner=play(boards,draws[card], marks)
        card+=1
    return winner

def lose_bingo(draws,boards):
    marks=[]
    for b in boards:
        marks.append([ [0 for row in range(len(b[0])) ] for col in range(len(b)) ] )
    #print(marks[0])    
    card=0;
    winner=()
    played=()
    while card<len(draws): 
        played=play(boards,draws[card], marks)
        if played: 
            winner=played
            played=()
            print(winner)
        card+=1
    return winner


draws,boards = read_boards()
#print(draws)
# for board in boards:
#     print(board, '\n' )
winner = lose_bingo(draws,boards)
print(winner)
n=len(winner[0])
sum=0
for i in range(n):
    for j in range(n):
        if winner[2][i][j] == 0 :
            sum+=winner[0][i][j]
print(sum*winner[1])