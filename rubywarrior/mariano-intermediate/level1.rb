class Player
  def play_turn(warrior)
    dir = warrior.direction_of_stairs
    space = warrior.feel dir
    warrior.walk! dir if space.empty?
  end
end
