import turtle

backgroundcolor = "#18546A"

window = turtle.Screen()
t = turtle.Turtle()
window.bgcolor(backgroundcolor)
t.pensize(2)

for i in range(4):
	t.fd(100)
	t.rt(90)

window.exitonclick()


