import turtle

# Make Screen
win = turtle.Screen()
win.title("Ping Pong Joe") # Naming The Screen 
win.bgcolor("Black") # Background color of Screen
win.setup(width=800, height=600) # Size of Screen
win.tracer(0) # Turn off the Automatic update of Screen


# Madrab1
madrab1 = turtle.Turtle()
madrab1.speed(0) # Make the fastest speed of Move
madrab1.shape("square") # Make the shape of Madrab
madrab1.color("blue") # Color of Madrab1
madrab1.shapesize(stretch_wid=5, stretch_len=1) # Stretching
madrab1.penup()
madrab1.goto(-350,0) # Make in this place


# Madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0) # Make the fastest speed of Move
madrab2.shape("square") # Make the shape of Madrab
madrab2.color("red") # Color of Madrab1
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(350,0) # Make in this place

# Ball
ball = turtle.Turtle()
ball.speed(0) # Make the fastest speed of Move
ball.shape("square") # Make the shape of Madrab
ball.color("white") # Color of Madrab1
ball.penup()
ball.goto(0,0) # Make in this place
ball.dx = 0.5 #Changing of x
ball.dy = 0.5 #Changing of y


# Score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 | Player 2: 0", align="center", font=("Courier", 24, "normal"))


# Functions

# control Madrab1
def madrab1_up():
    y = madrab1.ycor() # Get the y of Madrab1
    y += 20 
    madrab1.sety(y) # Set the y of Madrab1 to the new y

def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)


def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)

# Keyboard bindings
win.listen() # Tell the window to expext keyboard input
win.onkeypress(madrab1_up, "w") # Call fun. of madrab1_up when pressing w
win.onkeypress(madrab1_down, "s")
win.onkeypress(madrab2_up, "Up")
win.onkeypress(madrab2_down, "Down")


# Making the Game
while True:
    win.update() # Update the Screen every time the game run

    # Move Ball
    ball.setx(ball.xcor() + ball.dx) # Starts at 0 and increasing x
    ball.sety(ball.ycor() + ball.dy) # Starts at 0 and increasing y

    # Border check
    # Y axis
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # X axis
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1: {} | Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} | Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))


    # Beating Madrab with Ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1 
   
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1 