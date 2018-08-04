l = (0..100).to_a.shuffle

puts "to sort", l.inspect

def simpleSort(list)
  sorted = []
  for item in list
    i = 0
    while (i<sorted.size && item>=sorted[i])
      i= i+1
    end
    if (i< sorted.size)
      sorted.insert(i, item)
      puts "sublist :", sorted.inspect
    else
      sorted.push item
    end
  end
  return sorted.inspect
end


puts "sorted: " , simpleSort(l).inspect
