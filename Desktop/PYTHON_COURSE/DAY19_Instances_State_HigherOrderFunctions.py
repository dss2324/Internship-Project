#More Turtle Graphics,Event Listners, State and Multiple Instances
#Turtle Event Listners :-enables us to listen what user want to do
from turtle import Turtle,Screen
timmy=Turtle()
screen=Screen()
def move_forwards():
    timmy.forward(10)
    
screen.listen() #screen will start listening
#once it  start listening we have to bind the particular function that is triggered when particular key is pressed
screen.onkey(key="space",fun=move_forwards)#imp don't use bracket in inside function in onkey() function
#use keyword arguments in function thatalready exists so to avoid confusion
#here onkey is higher order function bc it takes another function as input
#how onkey works
#onkey(key="space",fun=move_forwards):
#move_forwards(key)
#return move_forwards(key) 
screen.exitonclick()