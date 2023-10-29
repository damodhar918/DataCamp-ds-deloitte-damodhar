from turtle import Turtle, Screen

mark = Turtle()
screen = Screen()


def move_forwards():
    mark.forward(20)
    
def move_backwards():
    mark.backward(20)

def move_left():
    mark.left(20)
    
def move_right():
    mark.right(10)

def turn_left():
    mark.setheading(mark.heading() + 10)

def turn_right():
    mark.setheading(mark.heading() - 10)
    
def clear():
    mark.clear()
    mark.penup()
    mark.home()
    mark.pendown()

screen.listen()
screen.onkey(key="i", fun=move_forwards)
screen.onkey(key="k", fun=move_backwards)
screen.onkey(key="l", fun=turn_left)
screen.onkey(key="j", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()