import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
t.screensize(canvwidth=500, canvheight=300, bg="black")
tim.speed("fastest")
direction = [0, 90, 180, 270]
tim.pensize(5)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_walk(count):
    for _ in range(count):
        tim.color(random_color())
        tim.forward(20)
        tim.setheading(random.choice(direction))

random_walk(500)


screen = t.Screen()
screen.exitonclick()