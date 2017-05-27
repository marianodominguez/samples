#/usr/bin/env ruby

def pow(a,b)
  x = a
  pow = b
  while pow>1
   if pow.even?
      x= x * x
      pow = pow/2
   else
      x = a * x * x
      pow = pow/2
   end
  end
  x
end

puts pow 2,16
puts pow(2,64)-1