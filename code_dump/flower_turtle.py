import turtle
import math

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

def draw_petal(color, angle):
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.circle(100, 60)
        pen.left(120)
        pen.circle(100, 60)
        pen.left(120)
    pen.end_fill()
    pen.right(angle)

# Draw petals
colors = ["red", "orange", "yellow", "pink", "purple"]
for i in range(5):
    draw_petal(colors[i % len(colors)], 72)

# Draw flower center
pen.up()
pen.goto(-20, -30)
pen.down()
pen.fillcolor("yellow")
pen.begin_fill()
pen.circle(30)
pen.end_fill()

# Draw stem
pen.up()
pen.goto(0, -30)
pen.down()
pen.pensize(10)
pen.pencolor("green")
pen.right(90)
pen.forward(200)

pen.hideturtle()
screen.exitonclick()
