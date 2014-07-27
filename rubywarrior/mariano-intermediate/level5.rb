
class Player
  
  def initialize
      @action=0
      @plan = []
      @ticking = []
      @all_addr = [:forward, :left, :right, :backward]
  end
  
  def find_ticking warrior
    units = warrior.listen
    ticking = []
    units.each do |u|
      if u.ticking? ticking<<u
    end
    ticking
  end

  #gets path to ticking warrior if exists
  def make_path(warrior)
    units = warrior.listen
    @ticking = find_ticking warrior
    plan = [:left]
  end

  def avoid_fight warrior
    @all_addr.each do |a|
      space = warrior.feel a
      if space.empty?
        warrior.walk! a
        return true
      end
    end
    return false
  end

  def play_turn(warrior)
    @plan = make_path warrior
    current_dir = @plan[@action]
    current_dir = warrior.direction_of_stairs if current_dir.nil? 
    current_dir = warrior.direction_of @ticking[0] unless @ticking.empty?

    @ticking = find_ticking warrior

    if current_dir==:rest
      warrior.rest!
      @action +=1
      return nil
    end

    space = warrior.feel current_dir
    if space.enemy?
      fled = false
      fled = avoid_fight unless @ticking.empty?      
      warrior.attack! current_dir unless fled
      @action-=1
    end
    warrior.rescue! current_dir if space.captive?
    warrior.walk! current_dir if space.empty? or space.stairs?
    @action +=1
  end
end
  