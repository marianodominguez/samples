#!/usr/bin/env ruby

require "rubygems"
require "rubygame"

include Rubygame

@screen = Screen.open [ 800, 600 ]
@venomSheet = Surface.load "resources/Venom.png"
@venomFrames = {
  :walking => [[57, 162, 154, 125],  [218, 162, 154, 125],
  [370, 162, 132, 118], [506, 162, 132, 118], [640, 165, 132, 118]]
}

class Venom
  def initialize(args)
    super()
    @image = @venomSheet[:walking][0]
    @rect  = @image.make_rect

  end

  def update  seconds_passed

  end

  def draw  on_surface
    @image.blit  on_surface, @rect
  end

end
