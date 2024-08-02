from turtle import Turtle,Screen
import turtle
import random
#Drawing Spirograph
timmy=Turtle()
turtle.colormode(255)
directions=[0,90,180,270]
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    #Generating  our Tuple
    my_tuple=(r,g,b) 
    return my_tuple #returning my_tuple

def draw_spirograph(size_of_gap):
    
    for i in range(int(360/size_of_gap)):
    
        timmy.speed(0)
        timmy.pencolor(random_color()) 
        timmy.circle(100)
        current_heading=timmy.heading()
        timmy.setheading(current_heading+size_of_gap)
        
draw_spirograph(5)        
    
   
my_scrren=Screen()
my_scrren.exitonclick()