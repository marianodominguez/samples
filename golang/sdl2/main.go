package main

import "github.com/veandco/go-sdl2/sdl"

const WIDTH = 1200
const HEIGHT = 750

func main() {
	mandelbrot()
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
