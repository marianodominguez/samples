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
