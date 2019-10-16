#Spencer Paquette 10/15/19
import turtle
import random
bob = turtle.Turtle()
for x in range(0,5):
    color = hex(random.randint(0,16777215))
    bob.color("#" + color[2:])
    bob.begin_fill()
    bob.circle(25)
    bob.end_fill()
    bob.up()
    bob.forward(50)
    bob.down()
    
