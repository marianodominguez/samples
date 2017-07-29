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

puts "a = #{'a'.ord}"
puts "z = #{'z'.ord}"

msg = codes[0][:codes].split(' ')
key = codes[0][:weather]
i=0
keystring = []
final = []
msgstring = []

for c in msg do
  char = '|'
  unless c== '|' then
    offset =  key.chars.to_a[i % key.size ]
    keystring << offset
    decoded = (c.to_i + offset.ord)
    char = decoded % 'z'.ord
    char += 'a'.ord-1 if char <= 'a'.ord
    final << char.chr
    i+=1
  end
  i=0 if c=='|'
  msgstring << c.to_i
end
puts msgstring.join(',')
puts keystring.join(',')
puts final.join(',')