n=24
l=8
r=16
o=0
for i in (r-l..n) do
    x = n-i
    puts "#{i}+#{x}" if i+x == n and l<=x and x<=r and i<=x
    o+=1
end

puts o

# notes for optimization
#r=58
#l=24

#n-r = 93-58 = 35
#range = l, r/2
#n=93
#
#93 = 35,58, 36,57 37,56 ...43,50 44,49 45,48 46,47
#r = 46-35 = 11
#
