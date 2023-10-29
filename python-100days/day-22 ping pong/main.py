from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#TODO: Create a screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 620)
screen.title("Pong")
screen.tracer(0)

#TODO: Create and move a paddle

r_paddle = Paddle(350,0)
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


#TODO: Create another paddle
l_paddle = Paddle(-350,0)
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, "s")

#TODO: Create the ball and make it move
ball = Ball()
#TODO: Keep score
score = Scoreboard()

while True:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    #TODO: Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #TODO: Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
 
        
    #TODO: Detect when paddle misses
    if ball.xcor() > 380 :
        ball.reset_position()
        score.l_point()
        
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        



screen.exitonclick()