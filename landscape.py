#$pencer Paquette 10/15/19
import turtle


groundLevel = turtle.window_height() / 2 * -1 + 100
def grass(x, y):
    grass = turtle.Turtle()
    grass.ht()
    grass.width(10)
    grass.up()
    grass.goto(x,y)
    grass.down()
    grass.color('green')
    grass.left(150)
    for i in range(0,3):
        grass.forward(50)
        grass.left(180)
        grass.forward(50)
        grass.left(120)

def ground():
    ground = turtle.Turtle()
    ground.ht()
    ground.up()
    ground.goto(turtle.window_width() / 2 * -1, turtle.window_height() / 2 * -1 + 100)
    ground.pencolor('green')
    ground.fillcolor('green')
    ground.down()
    ground.begin_fill()
    ground.forward(turtle.window_width())
    ground.right(90)
    ground.forward(100)
    ground.right(90)
    ground.forward(turtle.window_width())
    ground.right(90)
    ground.forward(100)
    ground.end_fill()

def tree(x, y):
    tree = turtle.Turtle()
    tree.ht()
    tree.up()
    tree.color('brown')
    tree.fillcolor('brown')
    tree.goto(x, y)
    tree.down()
    tree.begin_fill()
    for x in range(0,2):
        tree.forward(75)
        tree.left(90)
        tree.forward(325)
        tree.left(90)
    tree.end_fill()
    #leaves
    tree.up()
    tree.color('ForestGreen')
    tree.fillcolor('ForestGreen')
    height = groundLevel + 305
    tree.goto(x - 40, height)
    for x in range(0, 6):
        tree.down()
        tree.begin_fill()
        height = groundLevel + 325
        tree.circle(40)
        tree.end_fill()
        tree.up()
        tree.forward(60)
    tree.up()
    tree.goto(x, height + 20)
    for x in range(0, 4):
        tree.down()
        tree.begin_fill()
        height = groundLevel + 345
        tree.circle(40)
        tree.end_fill()
        tree.up()
        tree.forward(60)
    tree.up()
    tree.goto(x + 25, height + 45)
    for x in range(0, 3):
        tree.down()
        tree.begin_fill()
        height = groundLevel + 345
        tree.circle(40)
        tree.end_fill()
        tree.up()
        tree.forward(60)

        
def sky():
    sky = turtle.Turtle()
    sky.ht()
    sky.up()
    sky.color("LightSkyBlue")
    sky.fillcolor("LightSkyBlue")
    sky.goto(turtle.window_width() / 2 * -1, turtle.window_height() / 2)
    sky.down()
    sky.begin_fill()
    sky.forward(turtle.window_width())
    sky.right(90)
    sky.forward(turtle.window_height())
    sky.right(90)
    sky.forward(turtle.window_width())
    sky.right(90)
    sky.forward(turtle.window_height())
    sky.end_fill()

sky()
ground()
grass(-110,groundLevel)
grass(240,groundLevel)
tree(65, groundLevel)
