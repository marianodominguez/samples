
class Player
  
  def initialize
    @action=0
	@plan = [:forward, :forward, :forward]
  end
  
  def play_turn(warrior)
    current_dir = @plan[@action]
    current_dir = warrior.direction_of_stairs if current_dir.nil? 

    space = warrior.feel current_dir
    if space.enemy?
      warrior.attack! current_dir
      @action-=1
    end
    warrior.walk! current_dir if space.empty? or space.stairs?
    @action +=1
  end
end
  