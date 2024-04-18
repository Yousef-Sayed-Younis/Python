import turtle

w = turtle.Screen()
w.bgcolor("#35bf56")
w.title("عيد اضحى سعيد")
w.tracer(0)

t = turtle.Turtle()


def sheepBody():
    t.color("white")
    for _ in range(12):
        t.right(30)
        t.begin_fill()
        t.circle(30)
        t.end_fill()
        t.forward(30)

    t.goto(t.pos()[0] - 15, t.pos()[1] - 120)
    t.begin_fill()
    t.circle(80)
    t.end_fill()


t.penup()
t.goto(0, -300)
t.pendown()
sheepBody()


t.goto(t.pos()[0] - 5, t.pos()[1] + 160)
t.color("#fddec8")
t.shape("circle")
t.begin_fill()
t.width(100)
t.right(90)
t.forward(35)
t.end_fill()

t.width(1)

t.penup()
t.goto(t.pos()[0] + 5, t.pos()[1] + 30)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(t.pos()[0] + 9, t.pos()[1])
t.pendown()
t.color("black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(t.pos()[0] + - 60, t.pos()[1])
t.pendown()
t.color("white")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(t.pos()[0] + 10, t.pos()[1])
t.pendown()
t.color("black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.speed(3)
t.width(3)

t.shape("classic")
t.penup()
t.goto(t.pos()[0] + 30, t.pos()[1] - 50)
t.pendown()
t.color("black")
t.left(50)

for i in range(8):
    t.left(9)
    t.fd(2)


t.penup()
t.left(230)
t.goto(t.pos()[0] - 8, t.pos()[1] - 5)
t.pendown()
for _ in range(5):
    t.right(20)
    t.fd(5)

t.penup()
t.left(120)
t.goto(t.pos()[0] + 20, t.pos()[1] + 8)
t.pendown()
for _ in range(5):
    t.left(20)
    t.fd(5)


def write():
    t.penup()
    t.goto(0, 0)
    t.color("white")
    t.write("كل عام وانتم بخير ", font=(
        "Aldhabi", 100, "italic"), align="center")


write()
t.hideturtle()
turtle.mainloop()
