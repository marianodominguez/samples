package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	z := 1.0
	const delta float64 = 0.000000000000000001
	prevz := 999999.0
	iterations := 0

	for math.Abs(z-prevz) > delta && iterations < 1000000 {
		prevz = z
		z = z - (z*z-x)/(2*z)
		iterations++
	}
	fmt.Println("iterations: ", iterations)
	return z
}

func newton() {
	fmt.Println(Sqrt(2))
	fmt.Println(Sqrt(15))
	fmt.Println(Sqrt(9))
}
