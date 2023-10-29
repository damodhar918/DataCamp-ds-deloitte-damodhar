from sys import flags
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreBoard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=640)
screen.bgcolor("black")
screen.title("DJ Snake Game")  # Title of the game
screen.tracer(0)  # Turn off the animation

#TODO: 1.Create a snake body
snake = Snake()

#TODO: 4.Create a food
food = Food() 

#TODO: 5.Create a score board
scoreInfo = Scoreboard()

#TODO 3.Turn the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")    
screen.onkey(snake.right, "Right")

    
#TODO 2.Create a snake movement
def runGame():
    flag = True
    while flag:
        screen.update()
        time.sleep(0.1)
        snake.move()
        
        #TODO 5.Detect collision with food
        if snake.head.distance(food) < 18:
            food.refresh()
            scoreInfo.increase_score()
            snake.extend()
            
            # print("nom nom nom")
        #TODO 6.Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -310:
            scoreInfo.reset()
            flag = False
        
        #TODO 7.Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10 :
                scoreInfo.reset()
                flag = False
                break

runGame()

def reset_and_runGame():
    snake.reset()
    runGame()
    
screen.onkey(reset_and_runGame, "space")
screen.exitonclick()