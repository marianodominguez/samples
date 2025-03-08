package main

import (
	"image/color"

	"github.com/veandco/go-sdl2/sdl"
)

func curve() {
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
	var xs, ys, z, scale float64
	scale = -100.0

	for running {
		for x := 0; x < WIDTH; x++ {
			for y := 0; y < HEIGHT; y++ {
				xs = float64(x - WIDTH/2.0)
				ys = float64(y - HEIGHT/2.0)
				z = (xs*xs - ys*ys) / scale
				colour := color.RGBA{0, (uint8)(z), (uint8)(z), 255}
				surface.Set(x, y, colour)
			}

			if !event() {
				running = false
				break
			}
		}
		scale += 1
		if scale == 0 {
			scale = 1
		}

		window.UpdateSurface()
		sdl.Delay(33)
		surface.FillRect(&rect, 0)
	}

	running = event()
	sdl.Delay(33)
}
