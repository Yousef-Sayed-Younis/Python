from turtle import *

wn = Screen()
t = Turtle()

wn.title("Why Do I See You in Everything")
wn.bgcolor('black')
t.speed(0)

# Flag
# Green Part
t.goto(-350, -200)
t.color('green')
t.begin_fill()
t.forward(700)
t.left(90)
t.forward(133.3)
t.left(90)
t.forward(700)
t.left(90)
t.forward(133.3)
t.end_fill()

# White Part
t.left(180)
t.forward(133.3)
t.color('white')
t.begin_fill()
t.forward(133.3)
t.right(90)
t.forward(700)
t.right(90)
t.forward(133.3)
t.right(90)
t.forward(700)
t.end_fill()

# Black Part
t.right(90)
t.forward(133.3 * 2)
t.right(90)
t.forward(700)
t.right(90)
t.forward(400)
t.right(90)
t.forward(700)
t.right(90)
t.forward(400)

# Red Part
t.color('firebrick')
t.begin_fill()
t.right(130)
t.forward(310)
t.right(100)
t.forward(310)
t.end_fill()


t.penup()
t.goto(0, -200)
t.left(230)

# Map
t.color('white')
t.begin_fill()
t.pendown()
t.left(5)
t.forward(20)
t.left(10)
t.forward(80)

t.left(40)
t.forward(10)
t.right(80)
t.forward(10)

t.left(40)
t.forward(20)
t.color('black')
t.forward(60)

t.right(75)
for i in range(65):
    if i >= 37:
        t.color('white')
    t.forward(3)
    t.left(1)

t.right(90)
t.forward(5)
t.right(60)
t.forward(10)
for i in range(30):
    t.left(5)
    t.forward(0.5)

t.forward(5)
t.right(10)
t.forward(20)
t.right(90)
t.forward(10)
t.right(10)
t.forward(5)
t.right(20)
t.forward(10)

for i in range(20):
    t.left(3)
    t.forward(0.75)

t.forward(5)
t.left(40)
t.forward(10)
t.left(40)
t.forward(20)
t.right(90)
t.forward(10)
t.right(60)
t.forward(10)
t.left(45)
t.forward(6)

t.right(100)
t.forward(45)
t.left(30)
t.forward(30)
t.right(70)
t.forward(20)
t.left(45)
t.forward(40)
t.right(20)
t.color('black')
t.forward(10)
t.left(40)
t.forward(10)
t.right(20)
t.forward(90)


t.right(30)
t.forward(30)
t.color('white')
t.forward(30)
t.left(40)
t.forward(10)
t.right(20)
t.forward(5)
t.right(20)
t.forward(10)
t.left(40)
t.forward(10)
t.right(40)
t.forward(20)
t.left(20)
t.forward(20)
t.right(20)
t.forward(30)
t.right(10)
t.forward(15)
t.right(20)
t.forward(10)
t.end_fill()


# Writing
t.color('black')
t.penup()
for i in range(12):
    t.goto(30, 70 + (10 * i))
    t.write("Why Do I See You in")

t.color('green')
t.penup()
for i in range(13):
    t.goto(-30, -80 + (-10 * i))
    t.write("Why Do I See You in Everything")

t.hideturtle()
done()