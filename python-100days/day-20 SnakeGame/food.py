from turtle import Turtle
import random
FOOD_RANGE = 270
class Food(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("pink")
        self.speed("fastest")
        random_x = random.randint(-FOOD_RANGE, FOOD_RANGE)
        random_y = random.randint(-FOOD_RANGE, FOOD_RANGE)
        self.goto(random_x, random_y)
        self.refresh()
    
    
    def refresh(self):
        random_x = random.randint(-FOOD_RANGE, FOOD_RANGE)
        random_y = random.randint(-FOOD_RANGE, FOOD_RANGE)
        self.goto(random_x, random_y)  