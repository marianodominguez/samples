
class Player
  
  def initialize
      @bound=0
  end
  
  def bind_all warrior, bound
    all_dirs = [ :forward, :backward, :right, :left]
    dir = all_dirs[bound]
    space = warrior.feel dir
    warrior.bind! dir if space.enemy?
    warrior.rescue! dir if space.captive?
  end
  
  def exitlevel
  end
  
  def play_turn(warrior)
    action=false
    if @bound<3
      bind_all warrior, @bound
    elsif @bound == 3 and (warrior.feel :left).enemy?
      warrior.attack! :left
      @bound-=1
    elsif @bound == 4
      warrior.rest!
    else
      dir = :left
      stairs = warrior.feel warrior.direction_of_stairs
      dir = warrior.direction_of_stairs if stairs.empty?
      space = warrior.feel dir
      warrior.attack! dir if space.enemy? 
      warrior.walk! dir if space.empty? or space.stairs?
    end
    @bound +=1
  end
end
