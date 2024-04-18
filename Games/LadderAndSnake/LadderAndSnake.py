import time
import turtle
import random

# Global Variables
PLS = []
TURNS = [0]
PLAY = True
SHAPES = ['classic', 'arrow', 'turtle', 'circle', 'square', 'triangle']


# Make Screen
w = turtle.Screen()
w.title("Ladder and Snake")
w.bgcolor("purple")
w.setup(width=800, height=800)
w.tracer(0)


# Background Colors
colors = ["yellow", "white", "red", "CornflowerBlue", "green"]
n = 0
for i in range(100):
    color = turtle.Turtle()
    color.speed(0)

    if i % 10 == 0 and i >= 10:
        n = random.randint(0, 4)

    color.color(colors[n])

    if n + 1 < 5:
        n += 1
    else:
        n = 0

    color.penup()
    color.goto(-360 + (i % 10) * 80, -360 + (i // 10) * 80)
    color.pendown()
    color.forward(40)
    color.left(90)
    color.forward(40)
    color.begin_fill()
    for i in range(4):
        color.left(90)
        color.forward(80)
    color.end_fill()
    color.hideturtle()


# Columns And Rows
for i in range(18):
    cAr = turtle.Turtle()
    cAr.color("black")
    cAr.penup()
    if i < 9:
        cAr.goto(-320 + 80 * i, 0)
    else:
        r = i - 9
        cAr.goto(0, -320 + 80 * r)

    cAr.pendown()
    cAr.pensize(5)

    if i < 9:
        cAr.left(90)

    cAr.forward(400)
    cAr.back(800)

w.update()

COLORS = ['sienna', 'purple4', 'Darkblue', "orange"]
SHAPES = ['classic', 'arrow', 'turtle', 'triangle']

NP = int(turtle.numinput("How Many Players?", "2~4", None, 2, 4))
for i in range(NP):
    PLS.append(turtle.Turtle())

    PLS[i].shape(random.choice(SHAPES))
    PLS[i].shape(SHAPES[int(turtle.numinput("Choose Your Object:",
                 "1/classic, 2/arrow, 3/turtle, 4/triangle", '1~4', 1, 4)) - 1])
    c = random.choice(COLORS)
    COLORS.remove(c)
    PLS[i].color(c)
    PLS[i].penup()
    PLS[i].shapesize(stretch_wid=2, stretch_len=2)
    PLS[i].showturtle()
    PLS[i].goto(-360, -360)


# Finish Word
f = turtle.Turtle()
f.hideturtle()
f.color("black")
f.penup()
f.goto(-360, 355)
f.write("Finish", align="center", font=['Arial', 15, "normal"])


# Numbers
t, d, l = 1, -5, 0
for i in range(100):
    r = 0
    number = turtle.Turtle()
    number.hideturtle()
    number.color("black")
    number.penup()

    if i % 10 == 0 and i >= 10:
        t *= -1
        r = 0.1
        if t == -1:
            l = 15
        else:
            l = 0

    number.goto((-340 + d * t + l) * t + t * (i % 10 - 0.1)
                * 80, -390 + (i // 10) * 79)
    number.write(i + 1, font=('Arial', 15, 'normal'))


# Make Snakes
n = 6
snakes = [f"C:/Users/Yousef Sayed/snake{i}.gif" for i in range(n)]
_ = [w.addshape(snakes[i]) for i in range(n)]

positions = [(-230, -15), (-225, 300), (10, 20),
             (260, -200), (100, 90), (-160, -40)]

for i in range(n):
    snake = turtle.Turtle()
    snake.shape(snakes[i])
    snake.penup()
    snake.goto(positions[i])


# Make Ladders
ladders = [f"C:/Users/Yousef Sayed/ladder{i}.gif" for i in range(n)]
_ = [w.addshape(ladders[i]) for i in range(n)]

positions2 = [(0, -320), (335, -250), (-320, -120),
              (125, 20),  (300, 220), (380, 420)]
for i in range(n):
    ladder = turtle.Turtle()
    ladder.shape(ladders[i])
    ladder.penup()
    ladder.goto(positions2[i])


# Make Dice
DICES = [f'C:/Users/Yousef Sayed/dice{i}.gif' for i in range(1, 7)]

_ = [w.addshape(DICES[i]) for i in range(6)]

dice = turtle.Turtle()
dice.shape(DICES[0])
dice.speed(0)
dice.shapesize(stretch_wid=1, stretch_len=1)
dice.goto(0, 0)
dice.penup()


# GO Down "Snakes"
places = [(200, -120), (-120, 40), (40, 200),
          (-360, 120), (120, 280), (-200, 360)]

bk_places = [(360, -280), (-360, -120), (120, -40),
             (120, -200), (-120, -280), (-120, 200)]

deg = [270, 0, 180, 270, 180, 0]


# Go Up "Ladders"

places2 = [(-120, -360), (280, -360), (-360, -280),
           (200, -200), (360, 40), (360, 200)]

up_places = [(120, -280), (360, -120), (-280, -40),
             (-40, 280), (200, 120), (360, 360)]

deg2 = [180, 90, 180, 0, 270, 0]


def go_up_back(p):
    x = round(p.pos()[0])
    y = round(p.pos()[1])

    if (x, y) in places:
        index = places.index((x, y))
        p.goto(bk_places[index])
        p.left(deg[index])

    elif (x, y) in places2:
        index = places2.index((x, y))
        p.goto(up_places[index])
        p.left(deg2[index])


def Pdice(*_):
    pos = (random.randint(-350, 350), random.randint(-350, 350))
    dice.goto(pos)
    num = random.randint(1, 6)
    dice.shape(DICES[num-1])
    move(num)


def winner(n):
    cs = [f"Victory Belongs to Player {n+1}", f"Player {n+1} is The Winner"]
    s = random.choice(cs)
    w.clear()
    win = turtle.Turtle()
    win.hideturtle()
    win.penup()
    win.goto(0, 0)
    win.write(s, font=["Arial", 40, "bold"], align="center")
    PLAY = False


def check_winner(n, pl):
    if (round(pl.pos()[0]), round(pl.pos()[1])) == (-360, 360):
        winner(n)


def move(num):
    w.tracer(1)
    n = TURNS.pop()
    pl = PLS[n]

    if n < len(PLS) - 1:
        n += 1
    else:
        n = 0

    TURNS.append(n)

    if pl.heading() == 180 and round(pl.pos()[1]) == 360 and pl.pos()[0] - 80 * num < -360:
        pass
    else:
        for _ in range(num):
            if round(pl.pos()[0]) == 360:
                pl.left(90)

            elif round(pl.pos()[0]) == -360 and round(pl.pos()[1]) != -360:
                pl.right(90)

            pl.forward(80)

    check_winner(n, pl)
    go_up_back(pl)


while PLAY:
    w.update()
    time.sleep(1)
    w.onclick(Pdice)
