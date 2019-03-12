#!/usr/bin/env python

import turtle

backgroundcolor = "#18546A"

window = turtle.Screen()
window.bgcolor(backgroundcolor)
window.delay(2)

t = turtle.Turtle()

def star(n):
  angle=180-360/n
  sides=(2*n if n%2==1 else n)
  for i in range(sides):
    t.fd(100)
    t.rt(angle)

t.ht()
t.pu()
t.rt(45)
t.fd(100)
t.lt(45)
t.pd()

for i in range(15):
  star(i+5)
  t.pu()
  t.bk(100+10*i)
  t.rt(36)
  t.pd()

t.st()
t.pu()
t.home()

window.exitonclick()
