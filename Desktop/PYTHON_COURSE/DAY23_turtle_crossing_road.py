import time
from turtle import Screen
from DAY23_player import Player
from DAY23_car_manager import CarManager
from DAY23_scoreboard import Scoreboard
screen=Screen()
player=Player()
score=Scoreboard()
car_manager=CarManager()
screen.setup(width=600,height=600)
screen.tracer(0)

#TODO1 Move the turtle with keypress
#TODO2 Create and move the cars
#TODO3 Detect collision with cars
#TODO4 Detect when turtle reaches the other side
screen.listen()
screen.onkey(player.move_up,"Up")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    score.update_scoreboard()

    #detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            score.game_over()

    #detect when turtle reaches otherside eg:-succesful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score.increase_level()
    
    
screen.exitonclick()