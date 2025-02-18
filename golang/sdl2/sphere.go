package main

import (
	"image/color"

	"github.com/veandco/go-sdl2/sdl"
)

func sphere() {
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
	var col uint8
	running := true
	var xs, ys, scale int32
	scale = 100

	for running {
		for x := 0; x < WIDTH; x++ {
			for y := 0; y < HEIGHT; y++ {
				xs = (int32)(x - WIDTH/2)
				ys = (int32)(y - HEIGHT/2)
				col = (uint8)(xs*xs/scale + ys*ys/scale)
				colour := color.RGBA{0, col, col, 255}
				surface.Set(x, y, colour)
			}

			if !event() {
				running = false
				break
			}
		}
		scale -= 1
		if scale == 0 {
			scale = -1
		}

		window.UpdateSurface()
		sdl.Delay(33)
		surface.FillRect(&rect, 0)
	}

	running = event()
	sdl.Delay(33)
}
