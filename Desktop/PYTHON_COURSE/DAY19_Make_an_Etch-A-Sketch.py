from turtle import Turtle,Screen
timmy=Turtle()
screen=Screen()
screen.listen()
#W=Forwards,S=Backwards,A=Counter-Clockwise(left),D=Clockwise(right) ,C=clear drawing
def move_forwards():
    timmy.forward(10)
def move_backwards():
    timmy.backward(10)
def move_left():
    new_heading=timmy.heading()+10  #imagine > this is 0 dg adding 10 counter clockwiswe will lift it up
    timmy.setheading(new_heading)
    
def move_right():
    new_heading=timmy.heading()-10 #imagine > this is 0 dg subtracting 10 clockwiswe will lift it down
    timmy.setheading(new_heading)
    
def clear_drawing():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
    
    
screen.onkey(key="W",fun=move_forwards)
screen.onkey(key="S",fun=move_backwards)
screen.onkey(key="A",fun=move_left)
screen.onkey(key="D",fun=move_right)
screen.onkey(key="C",fun=clear_drawing)
    
screen.exitonclick()