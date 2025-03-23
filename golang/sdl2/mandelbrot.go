package main

import (
	"image/color"
	"math/cmplx"

	"github.com/veandco/go-sdl2/sdl"
)

const MAX_ITERATIONS = 600

func mouseEvent() (bool, float64, float64, bool) {
	for event := sdl.PollEvent(); event != nil; event = sdl.PollEvent() {
		switch t := event.(type) {
		case *sdl.QuitEvent:
			println("Quit")
			return false, 0, 0, false
		case *sdl.MouseButtonEvent:
			if t.Type == sdl.MOUSEBUTTONDOWN {
				x := float64(t.X)
				y := float64(t.Y)
				return true, x, y, true
			}
		}
	}
	return true, 0, 0, false
}

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

func renderMandelbrot(surface *sdl.Surface, xmin, xmax, ymin, ymax float64) bool {
	var xs, ys float64
	for x := 0; x < WIDTH; x++ {
		for y := 0; y < HEIGHT; y++ {
			xs = float64(x)*(xmax-xmin)/WIDTH + xmin
			ys = float64(y)*(ymax-ymin)/HEIGHT + ymin
			o := orbit(xs, ys)

			surface.Set(x, y, gcolor(o))
		}

		if !event() {
			return false
		}
	}
	return true
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

	var zp_x = -0.99000003
	var zp_y = 0.277500001

	xmin := -2.5
	xmax := 1.2
	ymin := -1.5
	ymax := 1.5
	clicked := false
	renderMandelbrot(surface, xmin, xmax, ymin, ymax)
	window.UpdateSurface()

	for clicked == false {
		sdl.Delay(100)
		_, mouseX, mouseY, clicked := mouseEvent()
		if clicked {
			zp_x = float64(mouseX)*(xmax-xmin)/WIDTH + xmin
			zp_y = float64(mouseY)*(ymax-ymin)/HEIGHT + ymin
			println("click", zp_x, zp_y)
			break
		}
	}

	zp_x = -0.99000003
	zp_y = 0.277500001

	for running {

		running = renderMandelbrot(surface, xmin, xmax, ymin, ymax)

		window.UpdateSurface()

		sdl.Delay(33)
		surface.FillRect(&rect, 0)

		xmax = zp_x + (xmax-zp_x)/2
		xmin = zp_x - (zp_x-xmin)/2

		ymax = zp_y + (ymax-zp_y)/2
		ymin = zp_y - (zp_y-ymin)/2

		if xmax-xmin == 0 || ymax-ymin == 0 {
			running = false
		}
		if !running {
			break
		}
	}

}
