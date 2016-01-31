import turtle

backgroundcolor = "#18546A"

window = turtle.Screen()
t = turtle.Turtle()
window.bgcolor(backgroundcolor)

for i in range(4):
	t.fd(100)
	t.rt(90)

window.exitonclick()


