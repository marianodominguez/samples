package main

import (
    "fmt"
)

type ErrNegativeSqrt float64 {
}

func (e ErrNegativeSqrt) Error() string {
    return "Invalid Square root for negative"
}

func Sqrt(f float64) (float64, error) {

    z := 1.0
    const delta float64 = 0.000000000000000001
    prevz:=999999.0
    iterations := 0

    for math.Abs(z-prevz) > delta && iterations < 1000000 {
        prevz = z
        z = z - (z*z - x)/(2*z)
        iterations++;
    }
    fmt.Println("iterations: ",iterations)

    return 0, error
}

func main() {
    fmt.Println(Sqrt(2))
    fmt.Println(Sqrt(-2))
}
