#!/usr/bin/env python

import turtle
import tkinter

backgroundcolor = "#18546A"

window = turtle.Screen()
window.bgcolor(backgroundcolor)

t = turtle.Turtle()
t.pensize(2)

def poly(n,size):
  angle=360/n
  for i in range(n):
    t.fd(size)
    t.rt(angle)
colors=["SeaGreen1","orange","cyan","plum","yellow","green","gold"
	, "black"  ]
t.pu()
t.fd(90)
t.rt(90)
t.fd(120)
t.lt(90)
t.pd()

for i in range(10):
  t.pencolor(colors[i % len(colors)])
  poly(i+3, 70-5*i)
  t.pu()
  t.bk(120)
  t.rt(36)
  t.pd()

t.pu()
t.home()

window.exitonclick()
