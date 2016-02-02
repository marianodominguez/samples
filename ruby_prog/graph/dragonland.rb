require 'gosu'
include Gosu 

class Fractals < Gosu::Window
  def initialize(w=800, h=600)
    @w,@h = w,h
    @cx,@cy = 0,0
    @color = Color::GREEN
    @angle=0
    @scale = Math.sqrt(2)/2
    super(w, h )
  end

  def line(p1, p2, color)
    x1 = p1[0] + @w/2
    y1 = @h/2 - p1[1]
    x2 = p2[0] + @w/2
    y2 = @h/2 - p2[1]    
    draw_line(x1 , y1, color, x2, y2, color, 1)
  end

  def rt t
    @angle += t
  end

  def lt t
    @angle -= t
  end

  def fd size
      endx, endy = 
		@cx + Math.sin(@angle * Math::PI / 180.0)*size, 
		@cy + Math.cos(@angle * Math::PI / 180.0)*size
      line [@cx, @cy], [endx, endy], @color
      @cx,@cy=endx,endy
  end

  def dragon level, size, i
    if level == 1
      fd size
      rt 90*i
      fd size
    else
      lt 45
      dragon level-1, size*@scale, 1
      rt 90*i
      dragon level-1, size*@scale, -1
      rt 45
    end
  end
  
  def dragonland
	 colors = [Color::GREEN, Color::YELLOW, Color::BLUE, Color::WHITE]
	 @cx,@cy=300,300
	 @angle=90
	 rt 90
	 i=0
	 4.times do
		@color=colors[i]
		i+=1
		dragon 16,600,1
		rt 45
	 end
  end
  
  def draw
    dragonland
  end

end #class

app = Fractals.new
app.show
