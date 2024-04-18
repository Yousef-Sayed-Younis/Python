import turtle

wn = turtle.Screen()
t = turtle.Turtle()

wn.title('Gaza Under Attack')
wn.bgcolor('LightGray')
t.speed(0)
t.penup()
t.hideturtle()

t.color('black')
for i in range(10):
    for x in range(7):
        t.goto(-325 + 92 * x, 250 - 10 * i)
        t.write('#GazaUnderAttack')

t.color('white')
for i in range(10):
    for x in range(7):
        t.goto(-325 + 92 * x, 150 - 10 * i)
        t.write('#GazaUnderAttack')

t.color('green')
for i in range(10):
    for x in range(7):
        t.goto(-325 + 92 * x, 50 - 10 * i)
        t.write('#GazaUnderAttack')

t.color('firebrick')
text = '#GazaUnderAttack'
i = 0
for x in range(2, 60, 4):
    t.goto(-325, 250 - 10 * i)
    if x > 16:
        c = x // 16
        for w in range(1, c + 1):
            t.write(text)
            t.goto(-325 + 92 * w, 250 - 10 * i)
            t.write(text[:(x-16)])
            x -= 16
    else:
        t.write(text[:x])
    i += 1

i = 0
for x in range(58, 1, -4):
    t.goto(-325, 100 - 10 * i)
    if x > 16:
        c = x // 16
        for w in range(1, c + 1):
            t.write(text)
            t.goto(-325 + 92 * w, 100 - 10 * i)
            t.write(text[:(x-16)])
            x -= 16
    else:
        t.write(text[:x])
    i += 1

t.color('black')
t.goto(-15, -200)
t.write(text, False, 'center', ('', 50, ''))


turtle.done()