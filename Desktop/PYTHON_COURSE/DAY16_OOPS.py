#we can split larger tasks into smaller one
#Classes and Objects
#Constructing Objects  & Accessing their attributes & methods
#class name are written in pascal case :-CarBlueprint
#car=CarBluePrint() here car is object & CarBlueprint  is class & in this manner we intialize object
#import turtle
from prettytable import PrettyTable
from turtle import Turtle,Screen#here we have imported class directly from turtle module
#Intialising/constructing object of class Turtle
timmy=Turtle()#Turtle() is class
timmy.shapesize(2,3,5)
timmy.color('lightgreen') #give color to turtle animation 
timmy.shape("turtle")
timmy.speed(1)
timmy.forward(100)
#timmy.speed(3)
#timmy.home()
#timmy.pendown()
#timmy.circle(25)
#print(timmy) 
my_screen=Screen()
print(my_screen.canvheight ) #here canvheight is attribute of class Screen
my_screen.exitonclick() #it will allow our screen to remain until we click on screen 

table=PrettyTable()
table.add_column("pokemon",["pikacchu","squirtle","charmander"])
table.add_column("type",["electric","water","fire"])
table.align='l'

print(table)

