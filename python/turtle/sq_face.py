#!/usr/bin/env python
import turtle

backgroundcolor = "#18546A"

def square(size):
	for i in range(4):
		t.fd(size)
		t.rt(90)

def face():
	square(200)

	t.pu()
	t.fd(150)
	t.rt(90)

	t.fd(30)
	t.pd()
	square(30)

	#eye1
	t.pu()
	t.fd(90)

	#eye2
	t.pd()
	square(30)

	t.pu()
	t.rt(90)
	t.fd(100)
	t.lt(90)
	t.bk(100)

	#mouth
	t.pd()
	for i in range(2):
		t.fd(150)
		t.rt(90)
		t.fd(20)
		t.rt(90)

def antenna():
	t.fd(50)
	square(10)
	t.bk(50)

window = turtle.Screen()
t = turtle.Turtle()
window.bgcolor(backgroundcolor)
t.pensize(2)
t.pu()
t.lt(90)
t.fd(100)
t.rt(90)
t.pd()

face()
t.pu()
t.fd(50)
t.lt(90)
t.fd(150)
t.pd()

antenna()
t.pu()

t.rt(90)
t.fd(50)
t.lt(90)
t.pd()
antenna()

t.pu()
t.home()
t.bk(100)
t.rt(90)
t.fd(100)
t.lt(100)
t.pd()
t.circle(120)

window.exitonclick()
