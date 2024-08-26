from turtle import *
speed(11)

def drawPlanet(tamanho, cor_planeta):
    color(cor_planeta)
    pendown()
    begin_fill()
    for c in range(360):
        left(tamanho)
        forward(tamanho)
    end_fill()
    penup()
    
bgcolor("MidNightBlue")
penup()
backward(200)
right(90)
forward(200)
left(90)
drawPlanet(1, "Red")
forward(250)
drawPlanet(1, "Green")
left(50)
forward(200)
drawPlanet(1, "White")
backward(200)
drawPlanet(1, "LightPurple")

hideturtle()
done()