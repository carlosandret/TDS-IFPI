from turtle import *
from random import *
speed(11)

def local_aleatorio():
    penup()
    setpos( randint(-400,400) , randint(-400,400) )
    pendown()

def drawsquare(tamanho, cor):
    color(cor)
    pendown()
    begin_fill()
    for side in range(6):
        left(60)
        forward(tamanho)
    end_fill()
    forward(tamanho)
    
    begin_fill()
    for side in range(6):
        left(60)
        forward(tamanho)
    end_fill()
    forward(tamanho)
    
    begin_fill()
    for side in range(6):
        left(60)
        forward(tamanho)
    end_fill()
    
    backward(tamanho)
    left(90)
    forward(tamanho)
    right(90)
    
    begin_fill()
    for side in range(6):
        left(60)
        forward(tamanho)
    end_fill()
    penup()
    
def drawBird(tamanho, cor):
    color(cor)
    pensize(2)
    pendown()
    right(60)
    forward(tamanho)
    left(120)
    forward(tamanho)
    right(60)
    penup()


bgcolor("LightBlue")
for c in range(17):
    drawsquare(20, "white")
    local_aleatorio()

for c in range(30):
    drawBird(13, "Black")
    local_aleatorio()    



hideturtle()
done()