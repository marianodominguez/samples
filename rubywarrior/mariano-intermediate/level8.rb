
class Player
  
  def initialize
      @action=0
      @plan = []
      @ticking = []
      @captives = []
      @captive_enemies = []
      @all_addr = [:left, :right, :forward , :backward]
  end
  
  def find_ticking warrior
    units = warrior.listen
    @ticking = []
    @captives = []
    units.each do |u|
      @ticking <<u if u.ticking?
      @captives << u if u.captive? and !@captive_enemies.include? u.location 
    end
  end

  #gets path to ticking warrior if exists
  def make_path(warrior)
    units = warrior.listen
    find_ticking warrior
    plan = []
  end

  def enemies warrior
    n = []
    [:left, :right, :forward, :backward].each do |i|
      n << i if (warrior.feel i).enemy?
    end
    n
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
    current_dir = warrior.direction_of @captives[0] unless @captives.empty?
    current_dir = warrior.direction_of @ticking[0] unless @ticking.empty?

    find_ticking warrior

    if warrior.health <5 and enemies(warrior).size ==0 and @ticking.empty?
      warrior.rest!
      return nil
    end

    space = warrior.feel current_dir
    if space.enemy?
      fight warrior,current_dir
      @action-=1
    end
    if space.captive? and !@captive_enemies.include? space.location
      puts "rescue", space.location
      warrior.rescue! current_dir
    end
    warrior.walk! current_dir if space.empty? or space.stairs?
    @action +=1
  end

  def fight warrior,current_dir
    action = :attack
    enemies = enemies(warrior)
    look = warrior.look.select {|x| x.enemy?}
    if look.size >=2
      action = :boom
    elsif enemies.size >1 
      action = :bind
      @captive_enemies << (warrior.feel enemies[0]).location
      puts "captives: ", @captive_enemies.inspect
      bound = true
    elsif !@ticking.empty?
      action = :flee 
    end     

    warrior.attack! current_dir if action == :attack
    warrior.bind! enemies[0] if action == :bind
    warrior.detonate! current_dir if action == :boom
    avoid_fight warrior if action == :flee
  end

end #class
  