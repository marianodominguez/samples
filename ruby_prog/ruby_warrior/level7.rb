
class Player
  
  def initialize
      @action=0
      @plan = [ :right, :forward, :forward, :forward, :forward, :left, :backward, 
      :left, :backward, :left, :forward, :forward, :forward, :forward]
  end
  
  def play_turn(warrior)
    current_dir = @plan[@action]
    current_dir = warrior.direction_of_stairs if current_dir.nil? 

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
  