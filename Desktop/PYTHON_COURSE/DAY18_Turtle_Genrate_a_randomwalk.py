from turtle import Turtle,Screen
import random
colors=["tan2","RoyalBlue","SteelBlue","orange","PaleGreen3","Gold","BlueViolet","aquamarine4","coral","DeepSkyBlue","DeepPink3","DarkGoldenrod2","chocolate4","chartreuse1","DarkTurquoise","DarkMagenta","DarkOrchid","IndianRed"]
directions=[0,90,180,270]
timmy=Turtle()
timmy.shape("turtle")
for i in range(500):
    timmy.speed(0)
    j=10
    timmy.pensize(j)
    j+=5
    timmy.pencolor(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
    
    
  
my_screen=Screen()
my_screen.exitonclick()