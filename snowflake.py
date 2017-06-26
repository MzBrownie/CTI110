# Turtle graphics
# Snowflakes

import turtle
turtle.Screen()
ts = turtle.Screen()
ts.bgcolor("magenta")
jess = turtle.Turtle()
jess.pensize(8)
jess.speed(8)
matt = turtle.Turtle()
matt.pensize(4)
matt.speed(8)
matt.shape("turtle")
matt.pencolor("white")

for i in range(10):
    for i in range(2):
        jess.forward(100)
        jess.right(60)
        jess.forward(100)
        jess.right(120)
    jess.right(36)
    
matt.penup()
matt.forward(100)
matt.left(45)
matt.pendown()

def branch():
    for flakes in range(3):
        for flakes in range (3):
              matt.forward(30)
              matt.backward(30)
              matt.right(45)
        matt.left(90)
        matt.backward(30)
        matt.left(45)
    matt.right(90)
    matt.forward(90)

for flakes in range(8):
    branch()
    matt.left(45)

matt.pencolor("red")    
matt.penup()
matt.forward(30)
matt.pendown()

    

ts.exitlick()
