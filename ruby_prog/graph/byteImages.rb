#!/usr/bin/env ruby

require 'rubygems'
require 'rubygame'

include Rubygame

class ByteImages
    def initialize(w=800, h=800)
        @screen = Rubygame::Screen.new [w,h]
        @w,@h = w,h
        @screen.title = "byte function"
        @queue = Rubygame::EventQueue.new
        @queue.ignore = [ActiveEvent,MouseMotionEvent,MouseDownEvent]
    end

    def xor(x,y)
        return x^y
    end

    def fn(x,y)
        valfloat = 127 * Math.cos(x.to_f/5) + 127 * Math.sin(y.to_f/5)
        return valfloat.to_i
    end

    def gradient(x,y)
        return (x+y)/4
    end

    def waves(x,y)
        return x*y
    end

    def waves2(x,y)
        return ((x-255)**2 + (y-255)**2) / 10
    end

    def waves3(x,y)
        return ((x-255)**2 - (y-255)**2)
    end

    def waves4(xp,yp)
        x = xp - 255
        y = yp - 255
        return x**2 + y**2 - x*y
    end

    def draw_function
        v = Array.new(@w)
        for x in (0...@w) do
            v[x] = Array.new(@h)
            for y in (0...@h) do
                v[x][y] = fn(x, y) % 256
            end
        end
        return v
    end

    def draw_pixels(pixels)
        pixels.each_with_index do |col, x|
            col.each_with_index do |row, y|
                #puts [x,y], " = ", pixels[x][y]
                @screen.set_at( [x,y], [255-pixels[x][y], 255-pixels[x][y], 255 ])
            end
        end
    end

    def run
        exit = false
        pixels = draw_function
        draw_pixels pixels
        @screen.update
        while not exit do
            @queue.each do |event|
                case event
                when Rubygame::ActiveEvent
                    @screen.update
                when Rubygame::QuitEvent
                    exit = true
                end
            end
        end #while
    end #run
end #class

app = ByteImages.new 512,512
app.run
