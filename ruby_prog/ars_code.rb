#!/usr/bin/env ruby

codes = [
  { 
    weather: 'cloudy', 
    codes: '10 16 20 06 18 | 04 20 26 01 | 14 11 03 | 08 06 08 15 21 03'
  },
  {
     weather: 'sunny',
     codes: '08 12 02 20 16 23 13 06 | 05 03 09 15 22 05 03 11 | 13 14 16 16 01 26 22 16 03 | 19 08 07 21 13 06 19'
   },
  {
    weather: 'windy',
    codes:  '08 11 09 10 | 04 16 24 | 17 19 02 15 04 26 15 03 26 | 03 06 25 10 22 16 21'
  }
]

#test  weather as key

msg = codes[1][:codes].split(' ')
key = codes[1][:weather]
i=0

for c in msg do
  char = '|'
  unless c== '|' then
    offset =  key.chars.to_a[i % key.size ]
    print offset.ord, ','
    decoded = c.to_i 
    char = decoded
  end 
  #print char,' '
  i+=1
end

puts