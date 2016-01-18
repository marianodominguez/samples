require "gosu"

class WhackARuby < Gosu::Window
  def initialize
    super(800,600)
    self.caption = "Wack the Ruby"
    @player = Gosu::Image.new('resources/secret_squirrel.png')
    @background_image = Gosu::Image.new("resources/space.png",
      :tileable => true)
    @x=400
    @y=300
    @width=@player.width
    @height=@player.height
    @velx=3;
    @vely=3;
    @angle=1.0
  end

  def draw
    @angle = -1.0 if @velx<0
    @angle = 1.0  if @velx>0
    offset=0
    offset=@width if @angle==-1.0 
    @player.draw(@x - @width/2 + offset, @y - @height/2, 10, scale_x=@angle)
    @background_image.draw(0, 0, 0)
  end

  def update
    @velx=0
    @vely=0
    if Gosu::button_down? Gosu::KbLeft or Gosu::button_down? Gosu::GpLeft then
      @velx=-3
    end
    if Gosu::button_down? Gosu::KbRight or Gosu::button_down? Gosu::GpRight then
      @velx=3
    end
    if Gosu::button_down? Gosu::KbUp or Gosu::button_down? Gosu::GpUp then
      @vely=-3
    end
    if Gosu::button_down? Gosu::KbDown or Gosu::button_down? Gosu::GpDown then
      @vely=3
    end
    @velx=-@velx if @x<=@width/2 or @x>=800-@width/2
    @vely=-@vely if @y<=@height/2 or @y>=600-@height/2
    @x += @velx
    @y += @vely

  end
end

window = WhackARuby.new
window.show
