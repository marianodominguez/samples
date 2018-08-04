def profile_pow(a,n)
  @total=0
  rec_pow(a,n)
end

def rec_pow(a,n)
  @total +=1
  return a if n==1
  sub=rec_pow(a,n/2)
  return sub*sub if n.even?
  return sub*sub*a
end

puts profile_pow(2,10)
puts "o(n) #{@total}"
puts profile_pow(10,100)
puts "o(n) #{@total}"
puts profile_pow(2,64)
puts "o(n) #{@total}"
puts profile_pow(2,1000)
puts "o(n) #{@total}"
