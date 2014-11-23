#!/usr/bin/env ruby

require 'rubygems'
require 'rubygame'

include Rubygame


class ComplexPlane
  def initialize(w=800, h=800, xmax=1.0, ymax=1.0)
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
    valfloat = 127 * Math.cos(x.to_f * 0.05) + 127 * Math.sin(y.to_f * 0.05)
    return valfloat.to_i
  end

  def draw_function
    v = Array.new(@w)
    for x in (0...@w) do
      v[x] = Array.new(@h)
      for y in (0...@h) do
        v[x][y] = xor(x, y) % 256
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

app = ComplexPlane.new 512,512
app.run
