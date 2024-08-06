import math
import turtle
import random


def pick_color():
    colors = ["dark orchid", "dark magenta", "dark violet", "indigo",
              "blue violet", "medium orchid", "midnight blue", "purple"]
    random.shuffle(colors)
    return colors[0]
    # return "yellow"


def drawPetal(turtle, x, y):

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    random_color = pick_color()
    turtle.fillcolor(random_color)
    turtle.begin_fill()
    turtle.right(20)
    turtle.forward(70)
    turtle.left(40)
    turtle.forward(70)
    turtle.left(140)
    turtle.forward(70)
    turtle.left(40)
    turtle.forward(70)
    turtle.penup()
    turtle.end_fill()


def drawPhyllPattern(turtle, t, petalStart, angle=137.5077641, size=15, cSpread=5):
    phi = angle * (math.pi / 180.0)
    xCenter = 0.0
    yCenter = 0.0

    for n in range(0, t):
        if n <= 50:
            turtle.fillcolor("tan4")
        elif n > 50 and n <= 150:
            turtle.fillcolor("sienna")
        elif n > 150 and n < 200:
            turtle.fillcolor("DarkOrange4")
        r = cSpread * math.sqrt(n)
        theta = n * phi
        x = r * math.cos(theta) + xCenter
        y = r * math.sin(theta) + yCenter
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        turtle.setheading(n * angle)
        if n > petalStart - 1:
            drawPetal(turtle, x, y)
        else:
            turtle.stamp()


t = turtle.Turtle()
t.shape("circle")
t.shapesize(0.3)
window = turtle.Screen()
window.bgcolor("black")
t.speed(100)
drawPhyllPattern(t, 250, 200, 137.5077641)
t.penup()
t.hideturtle()

turtle.mainloop()
