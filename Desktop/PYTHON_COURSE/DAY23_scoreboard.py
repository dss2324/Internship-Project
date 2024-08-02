from turtle import Turtle,Screen
FONT=("Courier",15,"normal")
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280,270)
        self.level=1
        
    def update_scoreboard(self):
        self.clear()
        self.write(f'Level:{self.level}',align='left',font=FONT)    
        
    def increase_level(self):
        self.level+=1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.hideturtle()
        self.write("Game Over",align='center',font=FONT)    