package main

func Pic(dx, dy int) [][]uint8 {
	image := make([][]uint8, dx)
	for i := range image {
		col := make([]uint8, dy)
		image[i] = col
	}

	for x := 0; x < dx; x++ {
		for y := 0; y < dy; y++ {
			image[x][y] = uint8((x * y))
		}
	}

	return image
}

func picture() {
	pic.Show(Pic)
}
