'''
Justify a text

Justify a text to a given size

The text is justified to the given size by adding spaces between the words, 
adding a hyphen at the end of the line and adding a dot at the end of the text.

this is not final. refactoring by using a format row function is pending

'''

text = "this is an example text, for     justification. This should be nice formatted. Even long words like deoxyribonucleic."

# Justify a text to a given size
def format(text, size):

    # Split the text into words
    words = text.split()
    # Result list
    result=[]
    # Column counter
    col=0
    # Word counter
    i=0
    # Row list
    row = []
    # While there are words
    while i<len(words):
        n=len(words[i])
        #word is bigger than the size
        if n>=size:
            # Add the word to the row
            word=words[i]
            row.append(word[:size-2]+"-")
            # Add the row to the result
            result.append(word[:size-2]+"-")
            # Reset the row
            row=[]
            row.append(word[size-2:])
            # Reset the column counter
            col=n-size+3
            i+=1
            if i<len(words): n=len(words[i])
        # Add the word to the row
        while col+n < size and i<len(words):
            row.append(words[i])
            col+=n+1
            i+=1
            if i<len(words): n=len(words[i]) 
        # Reset the column counter
        if col >= size:
            col = size
        # Calculate the number of spaces
        nspaces = size - col
        
        sp=nspaces // len(row)
        # Format the row
        frow = ""
        if len(row)==1:
            # Add the word to the row
            frow+="."*(sp+1)
            frow+=row[0]
        else:
            # Format the row
            for j in range(len(row)):
                if j==0: 
                    frow+=row[j]+"."*(sp+1)
                else:
                    frow+="."*(sp+1)
                    frow+=row[j]

        print(row)
        print(sp)
        # Add the row to the result
        result.append(frow)
        # Reset the row
        row=[]
        # Reset the column counter
        col=0
    # Return the result
    return "|\n".join(result)

# Print the result
print(format(text, 11))