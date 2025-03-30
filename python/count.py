def count_letters(str):
    if not str:
        return []
    count = 0
    result = []
    current=str[0]
    for i in range(0, len(str)):
        chr = str[i]
        if chr == " ":
            continue
        if chr == current:
            count += 1
        else:
            result.append(f"{current}{count}")
            count = 1
            current = chr
    if count>0: result.append(f"{current}{count}")
    return result

print(count_letters("aaabbbcccccddddddaaf"))
print(count_letters("aaabbbcccccddddddaa"))
print(count_letters("    "))