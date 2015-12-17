require "gosu"

class WhackARuby < Gosu::Window
  def initialize
    super(800,600)
    self.caption = "Wack the Ruby"
    @image = Gosu::Image.new('./resources/secret_squirrel.png');
    @x=200
    @y=200
    @width=@image.width
    @height=@image.height
    @velx=3;
    @vely=3;
  end

  def draw
    @image.draw(@x-@width/2, @y-@height/2, 1)
  end

  def update
    @velx=-@velx if @x<=@width/2 or @x>=800-@width/2
    @vely=-@vely if @y<=@height/2 or @y>=600-@height/2
    @x += @velx
    @y += @vely

  end
end

window = WhackARuby.new
window.show
