#!/bin/env python

import turtle

backgroundcolor = "#18546A"

window = turtle.Screen()
window.bgcolor(backgroundcolor)

t = turtle.Turtle()
t.pensize(2)

def star(n):
  angle=720/n
  if n%2==0: angle=180-360/n
  for i in range(n):
    t.fd(100)
    t.rt(angle)

t.pu()
t.rt(90)
t.fd(200)
t.lt(90)
t.pd()

for i in range(10):
  star(i+5)
  t.pu()
  t.bk(100)
  t.rt(36)
  t.pd()

window.exitonclick()