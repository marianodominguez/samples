l = [100,34,1,5,6,56,7,9]

def simpleSort(list)
  sorted = []
  for item in list
    i = 0
    while (i<sorted.size && item>=sorted[i])
      i= i+1
    end
    if (i< sorted.size)
      sorted.insert(i, item)
      #puts sorted
    else
      sorted.push item
    end
  end
  return sorted
end


puts simpleSort(l)
