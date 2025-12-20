'''
Count the number of letters in a string
'''

def count_letters(str):
    # If the string is empty, return an empty list
    if not str:
        return []
    # Count the number of letters
    count = 0
    # Result list
    result = []
    # Current character
    current=str[0]
    # For each character in the string
    for i in range(0, len(str)):
        chr = str[i]
        # Skip spaces
        if chr == " ":
            continue
        # If the character is the same as the current character, increment the count
        if chr == current:
            count += 1
        # If the character is different, add the current character and count to the result
        else:
            result.append(f"{current}{count}")
            count = 1
            current = chr
    # Add the last character and count to the result
    if count>0: result.append(f"{current}{count}")
    # Return the result
    return result

# Test the function
print(count_letters("aaabbbcccccddddddaaf"))
print(count_letters("aaabbbcccccddddddaa"))
print(count_letters("    "))