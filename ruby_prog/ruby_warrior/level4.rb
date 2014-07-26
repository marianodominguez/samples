
class Player
  
  def initialize
      @action=0
      @plan = [:left, :forward, :forward, :right, :forward, :backward, :rest, :forward, :forward, :backward, :backward]
  end
  
  def play_turn(warrior)
    current_dir = @plan[@action]

    if current_dir==:rest
      warrior.rest!
      @action +=1
      return nil
    end

    space = warrior.feel current_dir
    if space.enemy?
      warrior.attack! current_dir
      @action-=1
    end
    warrior.rescue! current_dir if space.captive?
    warrior.walk! current_dir if space.empty? or space.stairs?
    @action +=1
  end
end
  