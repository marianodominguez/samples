#!/usr/bin/env ruby

# track median for an array, potentially for a stream

require "algorithms"

def median(e, l , r , m )
  if l.size == r.size
    if e<m
      l.push(e)
      m=l.max
    else
      r.push(e)
      m=r.min
    end
  end
  if l.size<r.size
    if e<m
      l.push(e)
    else
      l.push(r.pop)
      r.push(e)
    end
    m=(l.max + r.min )/2.0
  end
  if l.size>r.size
    if e<m
      m.push(l.pop)
      l.push(e)
    else
      r.push(e)
    end
    m=(l.max + r.min )/2.0
  end
  #puts " [#{l.size},#{r.size} ]"
  return m
end

r = Containers::MinHeap.new()
l = Containers::MaxHeap.new()

a = [1, 3, 4, 5, 6, 7, 8, 12 ,15 , 16]
m=0

puts a.to_s

for x in a
  puts median x,l,r,m
end
