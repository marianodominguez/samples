'''
Display a forest using turtle.
'''
import turtle

backgroundcolor = "#18546A"

window = turtle.Screen()
t = turtle.Turtle()
# Set the speed of the turtle
t.speed(0)
window.bgcolor(backgroundcolor)
t.pensize(2)
# Move the turtle to the top
t.right(90)

# Draw the tree top
def treeTop(size):
	for i in range(10):
		t.forward(size)
		t.right(90)
		t.penup()
		t.forward(10)
		t.left(90)
		t.back(size+5)
		t.pendown()
		size=size+10

# Draw the tree trunk
def trunk():
	t.pu()
	t.fd(60)
	t.rt(90)
	t.pd()

	for i in range(2):
		t.fd(60)
		t.rt(90)
		t.fd(20)
		t.rt(90)

def forest():
	#move the turtle to the beginning of the forest
	t.home()
	t.pu()
	t.fd(200)
	t.pd()
	# Draw the trees
	for i in range(10):
		size = 0
		treeTop(size)
		trunk()
		t.pu()
		t.setheading(90)
		t.fd(80)
		t.lt(90)
		t.fd(120)
		t.rt(90)
		t.pd()
		# have the turtle head back to the top
		t.rt(90)

# Draw the forest
forest()
t.pu()
t.home()
window.exitonclick()
