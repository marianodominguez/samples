text = "this is an example text, for     justification. This should be nice formatted. Even long words like deoxyribonucleic."

def format(text, size):
    words = text.split()
    result=[]
    
    col=0
    i=0
    row = []
    while i<len(words):
        n=len(words[i])
        #word is bigger
        if n>=size:
            word=words[i]
            row.append(word[:size-2]+"-")
            result.append(word[:size-2]+"-")
            row=[]
            row.append(word[size-2:])
            col=n-size+3
            i+=1
            if i<len(words): n=len(words[i])
        while col+n < size and i<len(words):
            row.append(words[i])
            col+=n+1
            i+=1
            if i<len(words): n=len(words[i]) 
        if col > size:
            col = size
        nspaces = size - col
        
        sp=nspaces // len(row)
        frow = ""
        if len(row)==1:
            frow+="."*(sp+1)
            frow+=row[0]
        else:
            for j in range(len(row)):
                if j==0: 
                    frow+=row[j]+"."*(sp+1)
                else:
                    frow+="."*(sp+1)
                    frow+=row[j]

        print(row)
        print(sp)
        result.append(frow)
        #print(result)
        row=[]
        col=0

    return "|\n".join(result)

print(format(text, 11))