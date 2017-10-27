#!/usr/bin/env ruby

#24,4=17
#22,16=7
#8,25=4

#Y+4=T
#W+16=H
#I+25=E

codes = [
  { 
    ep: 1,
    type: "blue",
    weather: 'cloudy', 
    codes: '10 16 26 06 18 | 04 20 26 01 | 14 11 03 | 08 06 08 15 21 03'
  },
  { 
    ep: 2,
     type: "blue",
     weather: 'sunny',
     codes: '08 12 02 20 16 23 13 06 | 05 03 09 15 22 05 03 11 | 13 14 16 16 01 26 22 16 03 | 19 08 07 21 13 06 19'
   },
  { 
    ep: 3.1,
    type: "blue",
    weather: 'windy',
    codes:  '03 23 02 07 | 07 10 02 18 17 18 05 23 01 22 | 11 01 09 01 | 22 15 17 09 07'
  },
 { 
    ep: 3.2,
    type: "red",
    weather: 'windy',
    codes:  '08 11 09 10 | 04 16 24 | 17 19 02 15 04 26 15 03 26 | 03 06 25 10 22 16 21'
  },  
  { 
    ep: 4,
    type: "red",
    weather: 'cloudy',
    codes:  '17 11 | 04 14 | 18 11 10 03 | 20 18 11 24 02 08 08 19 | 19 17 06 11'
  },
  { 
    ep: 5,
    type: "blue",
    codes:  '21 22 12 01 | 17 13 05 23 13 19 22 26 | 06 02 21 25 07 02 | 08 26 23 23 | 02 26 26 23 13 12 25 01 | 09 19 09 12 18 | 20 26 08 23',
    weather: 'thunderstorms'
  },
  { 
    ep: 6,
    type: "red",
    codes: '20 18 01 01 24 04 07 09 22 | 10 23 25 17 03 14 09 08',
    weather: 'foggy'
  },
  { 
    ep: 7,
    type: "blue",
    codes: '21 25 15 25 15 10 | 01 06 | 01 22 01 | 23 12 10 24 08 17 01',
    weather: 'showers'
  },
  { 
    ep: 8,
    type: "red",
    codes: '17 11 23 15 11 05 16 | 26 06 | 19 23 18 | 07 20 16 07 04 02 | 07 21 21 05',
    weather: 'showers'
  },
  { 
    ep: 9,
    type: "blue",
    codes: '12 16 01 01 | 01 26 04 04 | 18 23 08 16 | 12 11 | 19 19 26',
    weather: 'showers'
  },
  { 
    ep: 10,
    type: "red",
    codes: '06 15 11 15 11 | 22 15 09 | 02 21 04 | 08 18 26 18 | 12 11',
    weather: 'clear'
  },
  { 
    ep: 11,
    type: "red",
    codes: '20 08 24 20 11 17 | 08 02 18 02 10 12 01 12 14 08',
    weather: 'foggy'
  },
  { 
    ep: 12,
    type: "red",
    codes: '17 22 16 04 | 19 16 11 18 16 23 | 19 09 22 | 23 05 | 13 23 17 13 19 25 24',
    weather: 'cloudy'
  },
  { 
    ep: 13,
    type: "red",
    codes: '07 25 19 | 11 15 05 10 | 24 15 08 15 | 22 24 26 04 06 12 11 14 22 02 | 15 12 08 22 05 | 04 17 26 15 25 01 04',
    weather: 'showers'
  },
  { 
    ep: 14,
    type: "blue",
    codes: '22 22 13 05 23 06 14 13 | 14 16 06 21 22 17 | 18 25 05 21 | 22 17 | 20 18 03 06 06 22 04',
    weather: 'rainy'
  },
  { 
    ep: 15,
    type: "red",
    codes: '23 25 17 21 | 14 12 24 20 16 | 20 04 16 | 21 16 20 | 04 | 10 21 26 06 | 08 23 18 01 04 23 | 06 18 | 16 09 08 | 01 01 24',
    weather: 'windy'
  },
  { 
    ep: 16,
    type: "blue",
    codes: '23 15 19 09 11 18 26 02 02 24 | 21 17 | 19 | 22 22 06 21 01 23',
    weather: 'stormy'
  },
  { 
    ep: 17,
    type: "red",
    codes: '21 26 09 19 04 04 10 07 | 21 07 06 23 21 04 10 | 01 19 10 22 | 01 01 18 22 06 17 | 08 05 19 14 08 11 15 20 11 22',
    weather: 'hail'
  },
  { 
    ep: 18,
    type: "red",
    codes: '14 12 02 22 19 | 14 17 | 08 | 15 19 21 23 22 | 05 05 20 05 10 16',
    weather: 'thunderstorms'
  },
   { 
    ep: 19,
    type: "red",
    codes: '26 25 05 | 18 24 13 22 21 | 22 02 02 | 08 05 10 11 20 | 22 18 23 15 01 16 25 20 13',
    weather: 'hurricane'
  }
]

def make_key(key, msg, type='blue')
  s=''
  for i in 0..msg.size
    s+=key[ i % key.size ]
  end
  s[msg.size-i]=key[(key.size-i) % key.size ] if type=='red'
  s
end

def decode(index, codes)
  #puts "a = #{'a'.ord}"
  #puts "z = #{'z'.ord}"
  msgstring=[]
  keystring=[]
  auxstring=[]
  final=[]
  keys=[]

  msg = codes[index][:codes].split(' ')
  key = codes[index][:weather]
  type = codes[index][:type] || 'blue'

  i=0
  for pair in msg do
    len = key.size()-1

    current_key=make_key(key, msg, type)[i]

    if pair !='|' then
      keystring << current_key
      keys << current_key.ord-97
      msgstring << pair.to_i - 1
       final << ( ( (msgstring[i] - keys[i])  % 26 ) + 97 ).chr
      i+=1
    else
      final << ' '
    end
  end

  puts keystring.join('')
  return final.join('')
end

for idx in 0..codes.size-1
  puts codes[idx][:ep]
  puts decode(idx,codes)
end