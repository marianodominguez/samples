def fib(n)
    u = 0
    v = 1
    x = v
    for i in 0 ... n
    x = v + u
    u = v
    v = x
    print v, " "
    end
    return v
end

fib(100)
