from curses import keyname


def read_data():
    result={}
    rules={}
    f = open("polymer_tst.txt","r")
    template=f.readline().strip()
    result['template']=template
    
    for line in f:
        if line.strip() !="":
            rule=line.strip().split(' -> ')
            pair=rule[0]
            out=rule[1]
            rules[pair]=out
    result['rules']=rules
    return result
            
def apply_rules(rules,polymer):
    result = []
    n=len(polymer)-1
    for i in range(n):
        pair=polymer[i]+polymer[i+1]
        if pair in rules:
            result.append(pair[0])
            result.append(rules[pair])
            if i==n-1 : result.append(pair[1])
    return "".join(result)


def counter(p):
    count={}
    for e in p:
        if e in count:
            count[e]+=1
        else:
            count[e]=1
    return count

def part1():
    nsteps=5
    d=read_data()
    polymer=d['template']
    rules=d['rules']

    for step in range(nsteps):
        print(step,polymer)
        polymer=apply_rules(rules,polymer)
        print(count_triplets(polymer))

    count=counter(polymer)        
    #print(count)
    
    r = max(count.values())-min(count.values())
    print(r)
   
def count_triplets(p):
    l=[]
    for i in range(len(p)-1):
        l.append(p[i]+p[i+1])
    return counter(l)

def addpair(e,d,prev):
    pv=prev[e] if e in prev else 1
    if e in d:
        d[e]+=pv
    else:
        d[e]=pv
    return d        
   
def part2():
    nsteps=5
    d=read_data()
    polymer=d['template']
    rules=d['rules']
    npairs={}
    for i in range(len(polymer)-1):
        pair=polymer[i]+polymer[i+1]
        if pair in npairs:
            npairs[pair]+=1
        else:
            npairs[pair]=1
    
    for step in range(nsteps):
        next={}
        for p in npairs.keys():
            if p in rules:
                new1=p[0]+rules[p]
                new2=rules[p]+p[1]
                next = addpair(new1,next, npairs)
                next = addpair(new2,next, npairs)
        print(npairs)
        npairs=next
    return npairs

def count_letters(npairs):
    result={}
    for p in npairs.keys():
        c1=p[0]
        c2=p[1]
        if c1 in result:
             result[c1]+=npairs[p]
        else:
            result[c1]=npairs[p]
        if c2 in result:
             result[c2]+=npairs[p] 
        else: 
             result[c2]=npairs[p]   
    return result

part1()
print('----')
npairs=part2()
print(npairs)
result = count_letters(npairs)
print(result)

