### Can you explain precisely the following snippet of code? Which drawing will you see?
import turtle
# toto = turtle.Screen()
# toto.bgcolor("black")
# titi = turtle.Turtle()
# titi.color("red")
# for i in range(3):
#     titi.right(90)
#     titi.circle(42)
# toto.exitonclick()

## Guess: A red turtle on a black background - it should draw three (red) circles of 42 degrees, turning 90 degrees each time from where it starts. 
### Answer, Correct
### note to self, turtle starts off in the positive x-axis direction

#Task 2.3 Using turtle, write a 
# function draw_polygon(sides) that takes an integer parameter sides.
# The function draws a regular polygon with the given number of sides:

def draw_polygon(sides):
    screen = turtle.Screen()
    screen.bgcolor("green")
    t = turtle.Turtle()
    t.color("yellow")
    length = 50
    degrees = 180 - ((sides-2) * 180)/sides
    for i in range(sides):
        t.left(degrees)
        t.forward(length)
    screen.exitonclick()


### Task 2.4 Using turtle, write a program to draw a spiral
def draw_spiral(steps):
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.color("white")
    degrees = 179
    for i in range(steps):
        t.forward(10)
        t.right(180-degrees+i/5)
    screen.exitonclick()
    

#draw_polygon(8)

draw_spiral(1000)

