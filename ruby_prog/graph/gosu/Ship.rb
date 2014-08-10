require 'gosu'
require_relative "player"

class GameWindow < Gosu::Window
  def initialize
    super 800, 600, false
    self.caption = "Gosu simple game"

     @background_image = Gosu::Image.new(self, "resources/Space.png", true)

     @player = Player.new(self)
     @player.warp(320, 240)
  end

  def update
  end

  def draw
     @player.draw
     @background_image.draw(0, 0, 0);
  end

  def button_down(id)
    if id == Gosu::KbEscape
      close
    end
  end

end

window = GameWindow.new
window.show