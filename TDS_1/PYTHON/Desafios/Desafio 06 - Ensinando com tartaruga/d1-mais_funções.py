from turtle import *

speed(0)
def drawstar():
    pendown()
    begin_fill()
    for side in range(4):
        left(90)
        forward(50)
    end_fill()
    penup()

color("WhiteSmoke")
bgcolor("MidnightBlue")

drawstar()
right(180)
forward(50)
left(90)
forward(100)
drawstar()
right(180)
right(90)
forward(50)
right(90)
forward(100)
drawstar()
left(90)
forward(100)
drawstar()
forward(100)
drawstar()
left(90)
forward(150)
drawstar()



hideturtle()
done()

