import colorsys
import turtle

s = turtle.getscreen()
s.bgcolor('#000033')

turtle.colormode(1.0)

t = turtle.Turtle()
t.speed(0)
t.shape('turtle')

for i in range(600):
    tint = i / 100.
    (rood, groen, blauw) = colorsys.hsv_to_rgb(tint, 1., 1)
    t.pencolor(rood, groen, blauw)
    t.forward(i / 2.)
    t.right(70)

t.hideturtle()
turtle.exitonclick()
