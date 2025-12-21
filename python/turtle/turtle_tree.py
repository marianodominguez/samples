'''
Draw a tree with a trunk and a top
'''
import turtle

backgroundcolor = "#18546A"

window = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
window.bgcolor(backgroundcolor)
t.pensize(2)

t.right(90)

size = 0
space = 0

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
#Turtle moves to the center of the screen, heading right
t.home()
treeTop(size)
trunk()

t.pu()
t.home()
# Wait for a mouse click to close the window
window.exitonclick()
