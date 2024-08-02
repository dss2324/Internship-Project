from turtle import Turtle
import random

#inheriting food class from turtle class
class Food(Turtle):  #here turtle is acting as super class
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        random_x=random.randint(-250,250)
        random_y=random.randint(-250,250)
        self.goto(random_x,random_y)
        