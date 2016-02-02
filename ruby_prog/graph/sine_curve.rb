#!/usr/bin/env ruby

require 'gosu' 

include Gosu

class SineCurve << < Gosu::Window
  
  def initialize(w=1920, h=1080)
    @w,@h = w,h
    @curves = [:circles, :cone, :polar, :sine]
    super(w,h, :fullscreen => true)
    self.caption = "Sine curve"
  end

  def draw_line(p1, p2, color)
    x1 = p1[0] + @w/2
    y1 = @h/2 - p1[1]
    x2 = p2[0] + @w/2
    y2 = @h/2 - p2[1]
    draw_line (x1, y1, color, x2, y2, color, 1)
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
      color = Color.rgba(224,124,242,255)
      draw_line( x1,y1, color, x,y, color, 1)
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
      color = Color.rgba(255,255,255,255)
      draw_line (x1, y1, color, x, y, color, 1)
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
      color = Color.rgba(200, 100, 255, 255)
      draw_line (x1, y1,color, x,y,color,1) 
      i += Math::PI / 180
    end
  end


  def sine
    color = Color.rgba(157,9,186, 255)
    (-@w/2..@w/2).each do |x|
      draw_line(0, @h/2,color,x , Math.sin(x.to_f/35)*100], color,1)
    end
  end

  def draw
    @curves.each do |c|
      @screen.fill [26, 20, 140], [0,0, @w, @h]
      self.send(c)
    end
  end
end

app = SineCurve.new
app.run
