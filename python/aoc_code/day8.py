def read_data():
    f = open("digits.txt","r")
    digits=[]
    values=[]
    for line in f:
        digits.append(line.split("|")[0].split())
        values.append(line.split("|")[1].split())

    return digits,values

def count_digits1(values):
    result=0
    for v in values:
        dl=list(filter(lambda x: len(x) in [2,4,3,7],v)) 
        result+=len(dl)
    return result    

def diff(s1,s2):
    set1=set(s1)
    set2=set(s2)
    return "".join(set1.difference(set2))

def decode(digits):
    result=[]
    for digit_line in digits:
        map={i:'' for i in range(0,10)}
        for du in digit_line:
            d ="".join(sorted(du))
            n=len(d)
            if n==2:
                map[1]=d
            elif n==4:
                map[4]=d
            elif n==3:
                map[7]=d
            elif n== 7:
                map[8]=d
        mid_left=diff(map[4], map[7])
        for d in [x for x in digit_line if len(x)==5 ]:
            d ="".join(sorted(d))
            if diff(mid_left, d) == "": 
                map[5]=d
            elif len(diff(d, map[1]))==3:
                map[3]=d
            else: 
                map[2]=d
        for d in [x for x in digit_line if len(x)==6 ]:
            d ="".join(sorted(d))
            if len(diff(d, map[5])) == 2:
                map[0]=d
            elif len(diff(d, map[1]))==4:
                map[9]=d
            else: 
                map[6]=d
        dmap = {map[n]:n for n in map.keys()}
        result.append(dmap)
    return result

def decode_values(map, values):
    digits=[]
    for num in values:
        snum="".join(sorted(num))
        digits.append(str(map[snum]))
    return "".join(digits)

digits,values = read_data()
decode_table=decode(digits)
sum=0
for i,v in enumerate(values):
    print(decode_table[i], v)
    v=decode_values(decode_table[i], v)
    #print(v)
    sum+=int(v)
print(sum)