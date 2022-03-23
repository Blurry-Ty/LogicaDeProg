import math
import turtle

janela = turtle.Screen()


don = turtle.Turtle()
don.color("Blue3")
don.shape("turtle")
don.speed(0)

def quadrado(x):
    don.fillcolor("Blue3")
    don.begin_fill()
    for quad in range(0,4):
        don.left(90)
        don.fd(x)
    don.end_fill()

def circ(y):
    don.fillcolor("white")
    don.begin_fill()
    don.circle(y)
    don.end_fill()

def ret():
    don.down()
    don.fillcolor("Blue3")
    don.begin_fill()
    don.fd(500)
    don.right(90)
    don.fd(36)
    don.right(90)
    don.fd(500)
    don.right(90)
    don.fd(36)
    don.end_fill()


#Primeiro Quadrado
quadrado(512/2)

#Escrita Maua
don.up()
don.left(90)
don.fd(64/2)
don.write("MAUA", move=False,align="left", font = ('Arial', 128, 'bold'))
don.left(180)
don.fd(64/2)
don.right(90)
don.fd(256/2)
don.right(180)

#Circulo Grande
don.down()
circ(256/2)

#Segundo Quadrado
don.fd(128*math.sqrt(2)/2)
don.left(90)
don.fd(74.98/2)
don.right(90)
quadrado(256*math.sqrt(2)/2)

#Circulo Grande
don.backward(128*math.sqrt(2)/2)
circ(256*math.sqrt(2)/4)

don.up()
don.fd(136)


ret()

don.up()

don.fd(220)
don.right(90)
ret()   

don.hideturtle()


janela.exitonclick()
turtle.TurtleScreen._RUNNING = True
