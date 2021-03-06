#!/usr/bin/env ruby

require 'rubygems'
require 'rubygame'

include Rubygame

class SineCurve
  
  def initialize(w=1920, h=1080)
    @w,@h = w,h
    @curves = [:circles, :cone, :polar, :sine]
    @screen = Rubygame::Screen.new [w,h], 0, 
		[Rubygame::HWSURFACE, Rubygame::DOUBLEBUF,Rubygame::FULLSCREEN]
    @screen.title = "Sine curve"
    @queue = Rubygame::EventQueue.new
    @queue.ignore = [ActiveEvent,MouseMotionEvent,MouseDownEvent]
    @aalias = false
    @aalias = true if @screen.respond_to?(:draw_line_a) 
  end

  def draw_line(p1, p2, color)
    x1 = p1[0] + @w/2
    y1 = @h/2 - p1[1]
    x2 = p2[0] + @w/2
    y2 = @h/2 - p2[1]
    if @aalias then
      @screen.draw_line_a [x1, y1], [x2, y2], color
    else
      @screen.draw_line [x1, y1], [x2, y2], color
    end
  end

  def polar
    px,py = nil,nil
    th=0.0
    while th<8*Math::PI do
      x = 300 * Math.cos(th)
      y = 300 * Math.sin(th)

      x1 = 500 * Math.cos(th)
      y1 = 500 * Math.cos(th)

      draw_line [x1,y1] , [x,y], [224,124,242]
      th += Math::PI / 200
    end
  end

  def cone
    i = 0.0
    while i<2*Math::PI do
      x = 300 * Math.sin(i)
      y = 300 * Math.cos(i)

      x1 = 100 * Math.sin(i)
      y1 = 100 * Math.cos(i)

      draw_line [x1, y1] , [x,y], [255, 255, 255]
      i += Math::PI / 180
    end
  end

   def circles
    i = 0.0
    while i<2*Math::PI do
      x = 500 * Math.sin(i)
      y = 500 * Math.cos(i)

      x1 = 200 * Math.cos(i)
      y1 = 200 * Math.sin(i)

      draw_line [x1, y1] , [x,y], [200, 100, 255]
      i += Math::PI / 180
    end
  end


  def sine
    (-@w/2..@w/2).each do |x|
      draw_line [0, @h/2], [x, Math.sin(x.to_f/35)*100],
      [157,9,186]
    end
  end

  def run
    @curves.each do |c|
      @screen.fill [26, 20, 140], [0,0, @w, @h]
      self.send(c)
      @screen.update
      @queue.wait
    end
  end
end

app = SineCurve.new
app.run
