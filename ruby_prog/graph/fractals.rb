#!/usr/bin/env ruby

require 'rubygems'
require 'rubygame'

include Rubygame

class Fractals
  def initialize(w=1200, h=600)
    @w,@h = w,h
    @shapes = [:sierpinski, :snow]
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
    @screen.draw_line [x1, y1], [x2, y2], color
  end

  def sierpinski
    px,py = @w/2,0
    line = [1]
    
    while py<@h do
      next_line = [0]
      line.each_with_index do |v, i|
        left_elem    = 0
        right_elem   = 0
        left_elem    = line[i-1] if i>0
        right_elem   = line[i+1] if i<line.size-1
        new_value    = (left_elem + v + right_elem)%2
        next_line << new_value
      end
      next_line << 0

      #puts line.inspect

      line.each_with_index do |v, i|
        x = px - line.size/2 + i
        @screen.set_at([x, py ], [255,255,255]) if v==1 and x>0 and x<@w
      end

      py+=1
      line = next_line
    end
  end

  def chaos
    rnd = Random.new
    xa = @w/2
    angle = 30 * (Math::PI/180)

    v = [ [xa, 0], [xa - @h* Math.tan(angle), @h ], [xa + @h*Math.tan(angle) , @h]] 

    x,y = rnd.rand(@w),rnd.rand(@h)
    for i in (0..500000) do
      vertex = v[rnd.rand(3)]
      mp = [ (vertex[0] + x ) /2, (vertex[1] + y)/2 ]
      @screen.set_at(mp, [255,255,255]) if 0<mp[0] and mp[0]<@w and 0<mp[1] and mp[1]<@h-1
      x,y = mp[0], mp[1]
    end
  end

  def snow_curve startp ,endp, level
    if level == 0 
      @screen.draw_line startp, endp, [255, 128, 255]
    else
      l = (endp[0] - startp[0])/3
      angle = 60 * (Math::PI/180)
      
      start_s1 = startp
      end_s1 = [(startp[0] + endp[0])/3, endp[1]]
      snow_curve(start_s1, end_s1, level-1)

      start_s2 = end_s1
      end_s2 = [start_s2[0] + l/2, start_s2[1] - l/2 * Math.tan(angle)]
      snow_curve(start_s2, end_s2, level-1)

      start_s3 = end_s2
      end_s3 = [start_s3[0] + l/2, start_s3[1] + l/2 * Math.tan(angle)]
      snow_curve(start_s3, end_s3, level-1)

      start_s4 = end_s3
      end_s4 = endp
      snow_curve(start_s4, end_s4, level-1)
    end
  end

  def snow
    snow_curve([0, @h/2], [@w , @h/2], 2)
  end

  def dragon
  end

  def run
    @shapes.each do |c|
      @screen.fill [26, 20, 140], [0,0, @w, @h] 
      self.send(c)
      @screen.update
      @queue.wait
    end
  end
end

app = Fractals.new
app.run
