
class Player
  
  def initialize
      @action=0
      @plan = []
      @ticking = []
      @captives = []
      @captive_enemies = []
      @all_addr = [:left, :right, :forward ]
  end
  
  def find_ticking warrior
    units = warrior.listen
    @ticking = []
    @captives = []
    @enemies = []
    units.each do |u|
      @ticking <<u if u.ticking?
      @captives << u if u.captive? and !@captive_enemies.include? u.location
      @enemies << u if u.enemy?
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

  def escape warrior
    n = []
    [:left, :right, :forward, :backward].each do |i|
      sp = warrior.feel i
      n << i if sp.empty? and !sp.stairs?
    end
    n
  end

  def avoid_fight warrior, current_dir
    @all_addr.each do |a|
      space = warrior.feel a
      if space.empty?
        warrior.walk! a
        return true
      end
    end
    warrior.attack! current_dir
    return false
  end

  def play_turn(warrior)
    @plan = make_path warrior

    current_dir = @plan[@action]
    current_dir = warrior.direction_of_stairs if current_dir.nil?
    current_dir = warrior.direction_of @enemies[0] unless @enemies.empty? 
    current_dir = warrior.direction_of @captives[0] unless @captives.empty?
    current_dir = warrior.direction_of @ticking[0] unless @ticking.empty?

    #avoid skipping level if captives
    step = warrior.feel current_dir
    avoid = escape warrior
    current_dir=avoid.first if step.stairs? and !@captives.empty?

    find_ticking warrior

    if warrior.health <=6 and enemies(warrior).size ==0 and @ticking.empty? and !@enemies.empty?
      warrior.rest!
      return nil
    end

    if warrior.health <=5 and enemies(warrior).size ==0 and !@enemies.empty?
      warrior.rest!
      return nil
    end

    if warrior.health <=3 and enemies(warrior).size >0
      escape = escape warrior
      warrior.walk! escape.first
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
    elsif space.captive? and @captive_enemies.include? space.location
       enemies = enemies(warrior)
       warrior.attack! enemies.sample unless enemies.empty?
       if enemies.empty?
          ex = warrior.direction_of_stairs
          ex = warrior.direction_of @captives[0] unless @captives.empty?
          escape = escape(warrior)
          ex = escape.sample 
          puts "escape is #{escape}"
          warrior.walk! ex 
        end
    end     
    warrior.walk! current_dir if space.empty? or (space.stairs? and enemies.empty?)
    @action +=1
  end

  def fight warrior,current_dir
    action = :attack
    enemies = enemies(warrior)
    look = warrior.look.select {|x| x.enemy?}
    if enemies.size >=3 and warrior.health > 7
      action = :bind
      @captive_enemies << (warrior.feel enemies[0]).location
      puts "captives: ", @captive_enemies.inspect
      bound = true
    elsif look.size >=2 and closest_captive(warrior) >=3
      action = :boom
    elsif !@ticking.empty?
      action = :flee 
    end
    puts "action is: #{action}"
    puts "there are #{enemies.size} enemies"
    warrior.attack! current_dir if action == :attack
    warrior.bind! enemies[0] if action == :bind
    warrior.detonate! current_dir if action == :boom
    avoid_fight warrior, current_dir if action == :flee
  end

  def closest_captive warrior
    dist = 1000
    @captives.each do |c|
      dist = warrior.distance_of c if warrior.distance_of(c) < dist      
    end
    dist
  end

end #class
  