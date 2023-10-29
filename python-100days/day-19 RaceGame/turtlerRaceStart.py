import random
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which colour turtle you want to bet?")
colors = ['red', 'green', 'blue', 'purple', 'orange', 'black']
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles= []

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_pos[turtle_index])
    all_turtles.append(new_turtle)
    
flag = True
while flag:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)
    
        if turtle.xcor() >= 220:
            flag = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(f'You lost! The {winning_turtle} turtle is the winner!')
                

screen.exitonclick()
