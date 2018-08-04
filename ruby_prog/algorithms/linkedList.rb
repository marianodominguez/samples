class Node
  attr_accessor :val,:next
  @val = nil
  @next = nil
  
  def initialize(v)
    @val=v
  end

end

class LinkedList
  
  def delete!(node)
    return if @head.nil?
    current = @head
    until current.next.val == node.val do
      current = current.next
      return if current.nil?
    end
    current.next = node.next
  end

  def add(node)
    if @head.nil?
      @head=node
      return
    end
    current = @head
    until current.next.nil? do
      current = current.next
    end
    current.next = node
  end

  def to_s
    return '[]' if @head.nil?
    s ='['
    current = @head
    until current.next.nil? do
      s += "#{current.val}, "
      current = current.next
    end
    s += "#{current.val}]"
    return s  
  end

end

a = Node.new('a')
b = Node.new('b')
c = Node.new('c')

l = LinkedList.new

puts l

l.add(a)
l.add(b)
l.add(c)
#l.add('d')
puts l

b = l.delete!(b)
puts l

c = l.delete!(c)

puts l

