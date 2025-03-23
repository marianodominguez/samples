package main

import (
	"fmt"
	"image/color"
	"math/cmplx"

	"github.com/veandco/go-sdl2/sdl"
	"github.com/veandco/go-sdl2/ttf"
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

func orbit(x float64, y float64) int {
	var d float64
	var z = complex(0, 0)
	var c = complex(x, y)
	var i int
	for i = 0; i < MAX_ITERATIONS && d <= 5.0; i++ {
		z = z*z + c
		d = cmplx.Abs(z)
	}
	return 10 - (i*10)/MAX_ITERATIONS
}

func gcolor(o int) color.Color {
	return gcolorGradient(o)
}

func gcolorSmooth(o int) color.Color {
	c := uint8(255 * o / 10) // Scale orbit value to hue (0-255)
	return color.RGBA{R: 0, G: c, B: c, A: 255}
}

func gcolorGradient(o int) color.Color {
	// Map the orbit value to a color gradient
	if o < 1 {
		return color.RGBA{R: 66, G: 30, B: 15, A: 255} // Dark brown
	} else if o < 2 {
		return color.RGBA{R: 25, G: 7, B: 26, A: 255} // Purple
	} else if o < 3 {
		return color.RGBA{R: 9, G: 1, B: 47, A: 255} // Dark blue
	} else if o < 4 {
		return color.RGBA{R: 4, G: 4, B: 73, A: 255} // Blue
	} else if o < 5 {
		return color.RGBA{R: 0, G: 7, B: 100, A: 255} // Light blue
	} else if o < 6 {
		return color.RGBA{R: 12, G: 44, B: 138, A: 255} // Cyan
	} else if o < 7 {
		return color.RGBA{R: 24, G: 82, B: 177, A: 255} // Light cyan
	} else if o < 8 {
		return color.RGBA{R: 57, G: 125, B: 209, A: 255} // Sky blue
	} else if o < 9 {
		return color.RGBA{R: 134, G: 181, B: 229, A: 255} // Pale blue
	} else {
		return color.RGBA{R: 211, G: 236, B: 248, A: 255} // White
	}
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

func renderText(surface *sdl.Surface, font *ttf.Font, text string, x, y int32) {
	color := sdl.Color{R: 255, G: 255, B: 255, A: 255} // White color
	textSurface, err := font.RenderUTF8Solid(text, color)
	if err != nil {
		panic(err)
	}
	textRect := sdl.Rect{X: x, Y: y, W: textSurface.W, H: textSurface.H}
	surface.Blit(&textRect, textSurface, nil)
}

func mandelbrot() {
	if err := sdl.Init(sdl.INIT_EVERYTHING); err != nil {
		panic(err)
	}
	defer sdl.Quit()

	if err := ttf.Init(); err != nil {
		panic(err)
	}
	defer ttf.Quit()

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
	font, err := ttf.OpenFont("/usr/share/fonts/truetype/ubuntu/UbuntuMono-B.ttf", 50) // Replace with the path to your font file

	surface.FillRect(&rect, 0)

	sdl.Delay(100)

	running := true

	// var zp_x = -0.990000029
	// var zp_y = 0.277500001

	var zp_x = -0.0
	var zp_y = 0.0

	xmin := -2.5
	xmax := 1.2
	ymin := -1.5
	ymax := 1.5
	clicked := false
	renderMandelbrot(surface, xmin, xmax, ymin, ymax)
	renderText(surface, font, fmt.Sprintf("Click to begin"), 10, 10)

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

	//Ignore click point for now
	zp_x = -0.990000029
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
