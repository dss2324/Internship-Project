#Creating a million dollar painting  sold in $1.25M
from turtle import Turtle,Screen
import turtle
import random

timmy=Turtle()
turtle.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    #Generating  our Tuple
    my_tuple=(r,g,b) 
    return my_tuple #returning my_tuple

timmy.setheading(225)
timmy.penup()
timmy.hideturtle()
timmy.forward(300)
timmy.setheading(0)
number_of_dots=101

for i in range(1,number_of_dots):
        timmy.dot(50,random_color())
        timmy.penup()
        timmy.forward(50)
        if i%10==0:
            timmy.setheading(90)
            timmy.forward(50)
            timmy.setheading(180)
            timmy.forward(500)
            timmy.setheading(0)

my_scrren=Screen()
my_scrren.exitonclick()