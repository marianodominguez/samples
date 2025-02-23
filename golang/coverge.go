package main

import (
	"fmt"
	"math"
)

func converge() {
	x1 := 0.9
	x2 := 0.9
	var y1, y2 = 0.0, 0.0
	for i := 0; i < 10000000; i++ {
		y1 = math.Cos(x1)
		x1 = y1
		y2 = math.Sin(x2)
		x2 = y2
		fmt.Printf("cos(x)=%.20f \t sin(x)=%.20f\n", y1, y2)
	}
}
