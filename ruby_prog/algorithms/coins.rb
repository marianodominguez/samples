
class ChangeUtil
  def min(amount, coins)
    min = []
    (amount+1).times{ |i| min[i]= 999 }
    min[0]=0

    result = [0]
    for i in 1..amount do
      result[i] = 0
      for j in 0..coins.size-1 do
        vj = coins[j]
        if vj <= i and min[i-vj] + 1 < min[i]
          min[i] = min[i - vj] + 1
          result[i] = vj
        end
      end
    end

    x = amount
    ncoins = []
    while x>0 do
      ncoins.push(result[x])
      x = x - result[x]
    end
    return ncoins
  end
end
