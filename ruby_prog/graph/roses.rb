#!/usr/bin/env ruby

require 'rubygems'
require 'rubygame'

include Rubygame

class Roses
	def initialize(w=800, h=600)
		@w,@h = w,h
		@roses = [1.0, 2.0, 3.0, 4.0, 5,0, 0.5, 2.0/5.0, 3.0/5.0, 1.0/3.0,
			 1.0/5.0, Math.sqrt(2), Math::PI]
		@screen = Rubygame::Screen.new [w,h], 0, 
			[Rubygame::HWSURFACE, Rubygame::DOUBLEBUF]
		@screen.title = "Sine curve"
		@queue = Rubygame::EventQueue.new
		@queue.ignore = [ActiveEvent,MouseMotionEvent,MouseDownEvent]
	end
	
	def draw_line(p1, p2, color)
		x1 = p1[0] + @w/2
		y1 = @h/2 - p1[1]
		x2 = p2[0] + @w/2
		y2 = @h/2 - p2[1]
		@screen.draw_line_a [x1, y1], [x2, y2], color
	end

	def rose(a=1.0)
		px,py = nil,nil
		th=0.0
		while th<32*Math::PI do
			r = 200 * Math.cos( a * th)
			x = r * Math.cos(th)
			y = r * Math.sin(th)
			draw_line [px,py] , [x,y], [255,20,255] if px!=nil
			px = x
			py = y
			th += Math::PI / 360
		end
	end

	def run
		@roses.each do |c|
			@screen.fill :black, [0,0, @w, @h] 
			rose(c)
			@screen.update
			@queue.wait
		end
	end
end

app = Roses.new
app.run
