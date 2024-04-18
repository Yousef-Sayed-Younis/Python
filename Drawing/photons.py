import turtle
import random

wn = turtle.Screen()
t = turtle.Turtle()

wn.setup(600, 800)
wn.title("Photons")
wn.bgcolor("black")

t.speed(0)
t.hideturtle()
t.penup()
t.width(10)
t.color("goldenrod2")


def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)


def heart():

    t.goto(0, -100)

    t.pensize(3)
    t.color("white")
    t.fillcolor("GhostWhite")
    t.begin_fill()
    t.pendown()
    t.left(140)
    t.forward(113)
    t.color("white")

    curve()
    t.left(120)
    curve()

    t.forward(112)
    t.color("white")
    t.end_fill()


t.pensize(2)
t.color("red")
n = 0
while n <= 10000:
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)

    if (x > 115 or x < -115) or (y > 200 or y < -200):
        t.goto(x, y)
        t.dot()
        n += 1

t.color("white")
t.goto(-115, -200)
t.pensize(5)
t.fillcolor("gold")
t.begin_fill()
t.pendown()
t.goto(115, -200)
t.goto(115, 200)
t.goto(-115, 200)
t.goto(-115, -200)
t.end_fill()

t.penup()
t.pensize(2)
t.color("gray40")
t.goto(-113, -198)
t.pendown()
t.goto(-113, 198)
t.goto(113, 198)

t.penup()
heart()

t.pensize(2)
t.fillcolor("gold3")
t.begin_fill()
t.forward(150)
t.goto(113, -198)
t.goto(0, -100)
t.end_fill()

turtle.done()
