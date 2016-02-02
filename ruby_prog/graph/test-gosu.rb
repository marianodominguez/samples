require 'gosu'
include Gosu

class MyWindow < Gosu::Window
  def initialize
  	@w=2304
  	@h=1440
    super(@w, @h, :fullscreen => true)
    self.caption = 'Hello World!'
  end

  def draw
  	for x in 0..@w/5
  		draw_line( @w/2, @h, Color::BLUE, x*5, 0, Color::YELLOW, 1)
  	end
  end

  def update
    if Gosu::button_down? Gosu::KbEscape then 
    	self.close
    end
  end
end

window = MyWindow.new
window.show
