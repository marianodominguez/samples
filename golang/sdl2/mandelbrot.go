package main

import (
	"image/color"
	"math/cmplx"

	"github.com/veandco/go-sdl2/sdl"
)

const MAX_ITERATIONS = 500

func orbit(x float64, y float64) float64 {
	var d float64
	var z = complex(0, 0)
	var c = complex(x, y)
	for i := 0; i < MAX_ITERATIONS && d < 4.0; i++ {
		z = z*z + c
		d = cmplx.Abs(z)
	}
	return d
}

func gcolor(o float64) color.Color {
	return color.RGBA{0, (uint8)(255 * o / 10), (uint8)(255 * o / 10), 255}
}

func mandelbrot() {
	if err := sdl.Init(sdl.INIT_EVERYTHING); err != nil {
		panic(err)
	}
	defer sdl.Quit()

	window, err := sdl.CreateWindow("test", sdl.WINDOWPOS_UNDEFINED, sdl.WINDOWPOS_UNDEFINED, WIDTH, HEIGHT, sdl.WINDOW_SHOWN)
	if err != nil {
		panic(err)
	}
	defer window.Destroy()
	rect := sdl.Rect{X: 0, Y: 0, W: WIDTH, H: HEIGHT}

	surface, err := window.GetSurface()
	if err != nil {
		panic(err)
	}
	surface.FillRect(&rect, 0)

	sdl.Delay(100)

	running := true
	var xs, ys float64

	xmin := -2.5
	xmax := 1.2
	ymin := -1.5
	ymax := 1.5

	for running {
		for x := 0; x < WIDTH; x++ {
			for y := 0; y < HEIGHT; y++ {
				xs = float64(x)*(xmax-xmin)/WIDTH + xmin
				ys = float64(y)*(ymax-ymin)/HEIGHT + ymin
				o := orbit(xs, ys)

				surface.Set(x, y, gcolor(o))
			}

			if !event() {
				running = false
				break
			}
			window.UpdateSurface()
		}

		sdl.Delay(33)
		surface.FillRect(&rect, 0)

		xmin += 0.1
		xmax -= 0.1

		ymin += 0.1
		ymax -= 0.1

		if !event() {
			running = false
			break
		}

		if xmax-xmin == 0 || ymax-ymin == 0 {
			running = false
		}

	}
}
