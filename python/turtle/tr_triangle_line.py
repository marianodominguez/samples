#!/usr/bin/env python
import turtle

backgroundcolor = "#18546A"

window = turtle.Screen()
t = turtle.Turtle()
window.bgcolor(backgroundcolor)
t.pensize(2)

t.right(90)

size = 100

for i in range(10):
	t.forward(size)
	t.right(90)
	t.penup()
	t.forward(10)
	t.left(90)
	t.back(size)
	t.pendown()
	size=size-10

t.pu()
t.home()
window.exitonclick()
