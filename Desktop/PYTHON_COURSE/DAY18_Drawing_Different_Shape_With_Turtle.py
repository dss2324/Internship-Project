from turtle import Turtle,Screen
import random
#Draw a triangle
timmy=Turtle()
timmy.shape("turtle")
#for i in range(3):
#    timmy.forward(100)
#    timmy.right(120)
    
#manual code for triangle    
#timmy.forward(100)
#timmy.right(120)
#timmy.forward(100)
#timmy.right(120)
#timmy.forward(100)

#Draw Hexagon
#for i in  range(6):
#    timmy.right(60)
#    timmy.forward(100)
    
    

#pentgon
#for i in  range(5):
#    timmy.right(72)
#    timmy.forward(100)
    
#timmy.right(60)
#timmy.forward(100)
#timmy.right(75)
#timmy.forward(100)
#timmy.right(75)
#timmy.forward(100)
#timmy.right(75)
#timmy.forward(80)
#timmy.right(60)
#timmy.forward(100)
   

#heptagon
#for i in range(7):
#    timmy.right(51.428)
#    timmy.forward(100)


#octagon
#for i in range(8):
#    timmy.right(45)
#    timmy.forward(100)


#nonagon
#for i in range(9):
#    timmy.right(40)
#    timmy.forward(100)

#decagon
#for i in range(10):
#    timmy.right(36)
#    timmy.forward(100)
 
 
 
#a function  that can create above all shape
colors=["tan2","RoyalBlue","SteelBlue","orange","PaleGreen3","Gold","BlueViolet","aquamarine4","coral","DeepSkyBlue","DeepPink3","DarkGoldenrod2","chocolate4","chartreuse1","DarkTurquoise","DarkMagenta","DarkOrchid","IndianRed"]
def draw_shape(num_sides):
    exterior_angle=360/num_sides
    for i in range(num_sides):
        timmy.pencolor(random.choice(colors))
        timmy.forward(100)
        timmy.right(exterior_angle)
            
#this loop will print all shapes  
for shape_side_n in range(3,11):
    j=10
    timmy.pensize(j)
    draw_shape(shape_side_n)
    
    
    
    
      
screen=Screen()
screen.exitonclick()