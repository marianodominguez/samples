'''
Sample code from Code Kata
https://www.codekata.com/data/04/weather.dat

Find the day with the smallest temperature spread

'''
from urllib import request
import re
min_spread=9999
mday=0

# Read the file
for l in request.urlopen("http://codekata.com/data/04/weather.dat"):
     line=l.decode().strip()

     # Parse the line
     columns=re.split('[\s]+', line)
     # Get the day
     day=str(columns[0])
     
     # Skip non-numeric lines
     if day.isnumeric():
        # Get the max and min temperatures
        max=columns[1].replace('*','')
        min=columns[2].replace('*','')
        spread=float(max)-float(min)
        #print(day, spread)
        # Update the minimum spread
        if spread<min_spread:
            min_spread=spread
            mday=day
print(mday,min_spread)
