#step1:-create a snake body by use of 3 squares
#step2:-Move the snake
#step3:-control the snake
#step4:-detect collision with food
#step5:-create a scoreboard
#step6:-detect collision with wall
#step7:-detect collision with tail

#here we are updating our snake game this is task of DAY24
#TODO1 create a screen setup  & snake body
from DAY20_Snake_Class import Snake
from DAY21_Food_class import Food
from DAY21_Scoreboard_class import Scoreboard
from turtle import Turtle,Screen
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #here screeen is off & will not show anything  until update method is called
snake=Snake()
food=Food()
score=Scoreboard()
screen.listen()


screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


#TODO2 Animating The snake segments on screen
i=0
game_is_on=True
while game_is_on:
    screen.update() #we only update screen once all segments are moved to their respective position
    time.sleep(0.1)
    snake.move()
    #detecting collision with food
    if snake.head.distance(food)<25:
        food.refresh()
        snake.extend()
        score.increase_score()
        
        
        
        
        
        
        
    score.update_scoreboard()    
    #detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
       score.reset()
       snake.reset()
    #detect collision with snakes tail
    #if head collides with any segment in the tail we triggers game over
    for segments in snake.segmentslist[1:]: #here we have use slicing & ommited 0th index
        if segments==snake.head:
            pass
        
        elif snake.head.distance(segments)<10:
            score.reset()
            snake.reset()
        
#TODO3 Create a Snake Class and move to OOP
#day20 snake class made
        
#TODO4 Controlling Snake with keypress

#TODO5 Detect collision with food

screen.exitonclick()

