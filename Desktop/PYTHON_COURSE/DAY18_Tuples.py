#Tuples are a data type,it is very similar to list but instead [] we use ()
#in tuples you can't change values like we can do in list nor you can remove any item
# we can convert a tuple into list using list(tuple_name)
from turtle import Turtle,Screen
import turtle

import random
directions=[0,90,180,270]
timmy=Turtle()
timmy.shape("turtle")
turtle.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    #Generating  our Tuple
    my_tuple=(r,g,b) 
    return my_tuple #returning my_tuple


for i in range(500):
    timmy.speed(0)
    j=10
    timmy.pensize(j)
    j+=5
    timmy.pencolor(random_color()) #passing random_colr() in pencolor
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

    
  
my_screen=Screen()
my_screen.exitonclick() 
