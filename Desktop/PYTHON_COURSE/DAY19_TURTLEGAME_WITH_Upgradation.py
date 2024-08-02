import turtle
from turtle import Turtle, Screen

# Instances mean two or more different objects of same class
# eg timmy.color() here colr assigned is the state of object
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make Your bet", prompt="Which turtle will win the race ? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


# print(all_turtles)

a=0
while is_race_on:
    count = 0
    
    winners = []
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if count == 3:
                winners.append(turtle.color())
                #print(winners)
                is_race_on = False
            
            count = count + 1
            
            for i in range(len(winners)):
                if winners[i]==user_bet:
                    print(f"You Have secured {i} position you have won ")
                    a=a+1
                    
            
        
            
        rand_distance = random.randint(0, 5)
        turtle.forward(rand_distance)

if(a==0):
    print("You have lost")   
                
screen.exitonclick()
