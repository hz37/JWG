# We gebruiken de turtle ('schildpad') module.

import turtle

# Verberg de schildpad.

turtle.hideturtle()

# Stel de achtergrond in.

s = turtle.getscreen()
s.bgcolor('#00ffff')

# Maak een schildpad.

t = turtle.Turtle()
t.speed(0)
t.pen(pencolor='#0000bb', pensize=3)

# Afstand tussen hokjes.

delta = 50

# Teken het hokjespatroon.

for i in range(10):
    for j in range(10):
        x = -250 + i * delta
        y = 250 - j * delta
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(x, y)
        t.goto(x + delta, y)
        t.goto(x + delta, y - delta)
        t.goto(x, y - delta)
        t.goto(x, y)
        t.penup()

# Verberg de schildpad.

t.hideturtle()

# Wacht tot iemand op het scherm klikt.

turtle.exitonclick()

