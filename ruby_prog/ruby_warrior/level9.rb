
class Player
  
  def initialize
      @action=0
      @plan = [ :bind, :left, :bind, :right, :detonate, :detonate,
      :rest, :rest, :forward, :left, :forward, :rest, :right, :right, :right, :forward]
  end
  
  def play_turn(warrior)
    current_dir = @plan[@action]
    current_dir = warrior.direction_of_stairs if current_dir.nil? 

  if current_dir==:bind
      @action +=1
      warrior.bind! @plan[@action]
      @action +=1
      return nil
    end

    if current_dir==:rest
      warrior.rest!
      @action +=1
      return nil
    end

    if warrior.health <=1  
      warrior.walk! :backward
      @plan[@action] = :rest
      return nil
    end

    if current_dir==:detonate
      warrior.detonate!
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
  