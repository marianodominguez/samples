package main

import (
	"image/color"

	"github.com/veandco/go-sdl2/sdl"
)

const WIDTH = 1200
const HEIGHT = 750

func main() {
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
			window.UpdateSurface()
		}
		if !event() {
			running = false
			break
		}
	}

	for running {
		running = event()
		sdl.Delay(33)
	}
}

func event() bool {
	for event := sdl.PollEvent(); event != nil; event = sdl.PollEvent() {
		switch event.(type) {
		case *sdl.QuitEvent:
			println("Quit")
			return false
			//break
		}
	}
	return true
}
