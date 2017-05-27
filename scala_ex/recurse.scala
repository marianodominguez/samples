def factorial(a: Int) : Int = {
  if (a==0) return 1 else return a*factorial(a-1)
}

println(factorial(3))
println(factorial(10))
