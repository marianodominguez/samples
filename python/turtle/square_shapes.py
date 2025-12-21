'''
Display square shapes using turtle.
'''

import turtle

# background color
backgroundcolor = "#18546A"

def square(size):
	for i in range(4):
		t.fd(100)
		t.rt(90)

window = turtle.Screen()
t = turtle.Turtle()
window.bgcolor(backgroundcolor)
t.pensize(2)

# squares
for i in range(10):
	square(60)
	t.rt(36)
	t.fd(100)

window.exitonclick()
