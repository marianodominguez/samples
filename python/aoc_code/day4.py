
def read_boards():
    f = open("bingo.txt","r")
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
    n=len(boards[0])
    result=()
    all_winners = {}
    for idx,board in enumerate(boards):
        if board:
            for row in range(n):
                for col in range(n):
                    e=board[row][col]
                    if e==card:
                        marks[idx][row][col]=1
                    if winner(marks[idx]): 
                        result=(board,card,marks[idx],idx)
                        all_winners[idx]=board
    print("winners:", all_winners)
    return result,all_winners


def bingo(draws,boards):
    marks=[]
    for b in boards:
        #print(b)
        #print("----")
        marks.append([ [0 for row in range(len(b[0])) ] for col in range(len(b)) ] )
    #print(marks[0])    
    card=0;
    winner=()
    all={}
    while not winner:
        winner,all=play(boards,draws[card], marks)
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
    all={}
    while card<len(draws) and len(boards)>0:
        print(len(boards), draws[card])
        played,all=play(boards,draws[card], marks)
        if played:
            winner=played
            #print(boards[winner[3]])
            boards= [ boards[i]  for i in range(len(boards)) if i not in all]
            marks = [ marks[i]   for i in range(len(marks)) if i not in all]    
        card+=1
    return winner


draws,boards = read_boards()
#print(draws)
# for board in boards:
#     print(board, '\n' )
winner = lose_bingo(draws,boards)
print("\tEND:", winner)
n=len(winner[0])
sum=0
for i in range(n):
    for j in range(n):
        if winner[2][i][j] == 0:
            sum+=winner[0][i][j]
print(sum*winner[1])