### Challenge: Using turtle and as few lines of code as possible, try to reproduce one (or more) of the following images.

### you can press a circle to get the flower shape.
import turtle
import math

screen = turtle.Screen()
screen.setup(1280, 720)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.color("white")

r_out = 200
r_in = 30
d = 190

t.goto((r_out-r_in)*math.cos(0) + d*math.cos(((r_out - r_in)/r_in)*0), (r_out-r_in)*math.sin(0) - d*math.sin(((r_out-r_in)/r_in)*0))

t.color("purple")

# x = (R−r)·cos t + d·cos(((R−r)/r)·t), y = (R−r)·sin t − d·sin(((R−r)/r)·t)




for i in range(10000):
    t.goto((r_out-r_in)*math.cos(i/100) + d*math.cos(((r_out - r_in)/r_in)*i/100), (r_out-r_in)*math.sin(i/100) - d*math.sin(((r_out-r_in)/r_in)*i/100))


# t.fillcolor("black")

# print(t.pos())
# t.goto(-screen.window_width()//4,-screen.window_height()//4)

# t.begin_fill()
# t.forward(screen.window_width() // 2)
# t.circle(40,90)
# t.forward(screen.window_height() // 2)
# t.circle(40,90)
# t.forward(screen.window_width() // 2)
# t.circle(40,90)
# t.forward(screen.window_height() // 2)
# t.circle(40,90)

# t.end_fill()


screen.exitonclick()





