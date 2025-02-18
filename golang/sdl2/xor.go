package main

import (
	"image/color"

	"github.com/veandco/go-sdl2/sdl"
)

func xor() {
	if err := sdl.Init(sdl.INIT_EVERYTHING); err != nil {
		panic(err)
	}
	defer sdl.Quit()

	window, err := sdl.CreateWindow("test", sdl.WINDOWPOS_UNDEFINED, sdl.WINDOWPOS_UNDEFINED, WIDTH, HEIGHT, sdl.WINDOW_SHOWN)
	if err != nil {
		panic(err)
	}
	defer window.Destroy()

	surface, err := window.GetSurface()
	if err != nil {
		panic(err)
	}
	surface.FillRect(nil, 0)

	var col uint8
	running := true

	for x := 0; x < WIDTH; x++ {
		for y := 0; y < HEIGHT; y++ {
			col = (uint8)(x ^ y)
			colour := color.RGBA{0, col, col, 255}
			surface.Set(x, y, colour)
		}

		if !event() {
			running = false
			break
		}
		window.UpdateSurface()
	}

	for running {
		running = event()
		sdl.Delay(33)
	}
}
