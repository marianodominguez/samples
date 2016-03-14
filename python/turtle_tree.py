import turtle

backgroundcolor = "#18546A"

window = turtle.Screen()
t = turtle.Turtle()
window.bgcolor(backgroundcolor)
t.pensize(2)

t.right(90)

size = 0
space = 0

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

treeTop(size)
trunk()

t.pu()	
t.home()
window.exitonclick()


