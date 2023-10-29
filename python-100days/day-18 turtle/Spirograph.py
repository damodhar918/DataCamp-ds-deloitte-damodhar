import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
'''# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'black', 'brown', 'grey','tan', 'violet', 'indigo', 'gold', 'silver', 'cyan', 'magenta', 'maroon', 'navy', 'olive', 'teal', 'aquamarine', 'azure', 'beige', 'coral', 'lavender', 'lime', 'orchid', 'plum', 'salmon', 'turquoise']
# t.screensize(canvwidth=500, canvheight=300,
#              bg="black")

########### Challenge 5 - Spirograph ########'''
tim.pensize(2)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()