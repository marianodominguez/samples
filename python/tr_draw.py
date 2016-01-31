#!/bin/env python

import turtle

backgroundcolor = "#18546A"
GOLDEN_PEN = (253,213,147)

turtle.mode("logo")
window = turtle.Screen()
window.bgcolor(backgroundcolor)

t = turtle.Turtle()
turtle.colormode(255)
t.pensize(2)

t.shape("turtle")
t.color("white")

t.pencolor(GOLDEN_PEN)


def star(n):
  for i in range(n):
    t.fd(200)
    t.rt(720/n)

for i in range(4):
  star(5)
  t.pu()
  t.bk(50)
  t.rt(90)
  t.pd()


#window.exitonclick()
