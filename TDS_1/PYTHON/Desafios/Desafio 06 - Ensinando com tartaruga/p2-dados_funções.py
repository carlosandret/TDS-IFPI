from turtle import *


def drawstar(starSize, starColour):
    color(starColour)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(starSize)
    end_fill()
    penup()

bgcolor("MidnightBlue")

drawstar(50, "Red")
forward(100)
drawstar(30, "White")
left(120)
forward(150)
drawstar(70, "Green")

hideturtle()
done()
 