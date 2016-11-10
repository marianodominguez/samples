a = 83748.to_s(2).split('')
puts a.join(',')
puts a.inject(0) { |v, x| (x=='0' and v<=2) ? v+=1: v}