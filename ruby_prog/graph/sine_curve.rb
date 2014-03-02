#!/usr/bin/env ruby

require 'rubygems'
require 'rubygame'

include Rubygame

class SineCurve
	def initialize(w=800, h=600)
		@w,@h = w,h
		@curves = [:sine, :cone, :polar]
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

	def polar
		px,py = nil,nil
		th=0.0
		while th<8*Math::PI do
			r = 200 * Math.cos((1.0/5.0) * th)
			x = r * Math.cos(th)
			y = r * Math.sin(th)

			x1 = 300 * Math.cos(th)
			y1 = 300 * Math.cos(th)

			draw_line [x1,y1] , [x,y], [20,0,255] 
			th += Math::PI / 100
		end
	end

	def cone
		i = 0.0
		while i<2*Math::PI do
			x = 100 * Math.sin(i)
			y = 100 * Math.cos(i)
			x1 = 200 * Math.cos(i)
			y1 = 200 * Math.sin(i)
			draw_line [x1,y1] , [x,y], [255,255,128]
			i += Math::PI / 180
		end
	end

	def sine
		(-@w/2..@w/2).each do |x|
			draw_line [0, @h/2], [x, Math.sin(x.to_f/35)*100],
				[255,0,255]
		end
	end

	def run
		@curves.each do |c|
			@screen.fill :black, [0,0, @w, @h] 
			self.send(c)
			@screen.update
			@queue.wait
		end
	end
end

app = SineCurve.new
app.run
