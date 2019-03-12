#!/usr/bin/env python

import turtle

backgroundcolor = "#18546A"

window = turtle.Screen()
window.bgcolor(backgroundcolor)

t = turtle.Turtle()
t.pensize(2)

def star(n,l):
  angle=720/n
  for i in range(n):
    t.fd(l)
    t.rt(angle)

t.pu()
t.rt(90)
t.fd(200)
t.lt(90)
t.pd()

for i in range(10):
  star(i+5,100-5*i)
  t.pu()
  t.bk(100)
  t.rt(36)
  t.pd()

t.pu()
t.home()

window.exitonclick()
