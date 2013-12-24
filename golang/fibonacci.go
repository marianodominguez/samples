package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {
    m,n := 0,1
    return func() int {
        sum := n + m
        n = m
        m = sum
        return sum
    }
    
}

func main() {
    f := fibonacci()
    for i := 0; i < 10; i++ {
        fmt.Println(f())
    }
}
