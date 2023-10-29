import turtle as t
import random
from imageColourRGB import image_colour_rgb as imgRGB


t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = imgRGB(r'C:\Users\jdamodhar\Desktop\python_essential-\python-100\day-18\image.jpg', 30)
tim.setheading(225)
tim.forward(280)
tim.setheading(180)
tim.forward(20)
tim.setheading(0)

for _ in range(9):
    for _  in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    
screen = t.Screen()
screen.exitonclick()