'''
Display polygons using turtle.
'''

import turtle

backgroundcolor = "#18546A"

sides = 4

def poly(size, sides):
	for i in range(sides):
		t.fd(100)
		t.rt(360/sides)

def draw():
	global sides
	t.clear()
	t.speed(0)
	for i in range(10):
		poly(60,sides)
		t.rt(36)
		t.fd(100)
	sides+=1
	if sides>10: t.bye()

window = turtle.Screen()
t = turtle.Turtle()
window.bgcolor(backgroundcolor)
t.pensize(2)
draw()
window.onclick(draw)
window.listen()
window.exitonclick()
