#!/bin/env python

import turtle

backgroundcolor = "#18546A"

window = turtle.Screen()
window.bgcolor(backgroundcolor)
window.delay(0)

t = turtle.Turtle()

def star(n):
  angle=180-360/n
  for i in range(n + n%2):
    t.fd(100)
    t.rt(angle)

t.pu()
t.fd(200)
t.rt(90)
t.fd(200)
t.lt(90)
t.pd()
t.ht()

for i in range(20):
  star(i+8)
  t.pu()
  t.bk(100)
  t.rt(36)
  t.pd()

t.st()
t.pu()
t.home()

window.exitonclick()
