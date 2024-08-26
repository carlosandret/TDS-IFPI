from turtle import *

def drawstar():
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(50)
    end_fill()
    penup()

color("WhiteSmoke")
bgcolor("MidnightBlue")

drawstar()
forward(100)
drawstar()
left(120)
forward(150)
drawstar()

hideturtle()
done()