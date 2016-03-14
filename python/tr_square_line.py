import turtle

backgroundcolor = "#18546A"

window = turtle.Screen()
t = turtle.Turtle()
window.bgcolor(backgroundcolor)
t.pensize(2)

t.right(90)

for i in range(10):
	t.forward(100)
	t.right(90)
	t.penup()
	t.forward(10)
	t.left(90)
	t.back(100)
	t.pendown()

t.pu()	
t.home()
window.exitonclick()


