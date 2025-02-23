package complex

import (
	"fmt"
	"math/cmplx"
)

func Cbrt(x complex128) complex128 {
	z := complex(1.0, 0)
	for i := 0; i < 100000; i++ {
		z -= (z*z*z - x) / (3 * x * x)
	}

	return z
}

func main() {
	fmt.Println(Cbrt(2))
	fmt.Println(cmplx.Pow(2.0, 0.33))
}
