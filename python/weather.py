from urllib import request
import re
min_spread=9999
mday=0

for l in request.urlopen("http://codekata.com/data/04/weather.dat"):
     line=l.decode().strip()

     columns=re.split('[\s]+', line)
     day=str(columns[0])
     if day.isnumeric():
        max=columns[1].replace('*','')
        min=columns[2].replace('*','')
        spread=float(max)-float(min)
        #print(day, spread)
        if spread<min_spread:
            min_spread=spread
            mday=day
print(mday,min_spread)
