
f = open("test2.txt","r")
measure = []
i = 0
diff=0
count=0
sumw=999999
sump=0

for line in f:
    measure.append(int(line))
    if i>=2:
        sump=sumw;
        sumw=sum([ measure[j] for j in range(i-2,i+1)])
        print(measure)
        #print(sumw,sump)
        diff=sumw-sump
        if diff>0: count+=1
    i+=1
    # if i>=6:
    #     i=0
    #     measure=measure[-3:]
print(count)