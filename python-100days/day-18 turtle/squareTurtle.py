from turtle import Turtle, Screen
import random
marker = Turtle()


color = ["black", "red", "green", "blue", "cyan", "yellow",  "magenta", 'orange', 'purple', 'brown', 'pink', 'gray', 'white']

marker.pensize(10)
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        marker.forward(100)
        marker.right(angle)


for n in range(3,11):
    marker.color(random.choice(color))
    draw_shape(n)
    


screen = Screen()
screen.exitonclick()