from turtle import Turtle,Screen
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        with open("DAY21_data.txt",mode='r') as file:
            self.highscore=(file.read())
        self.color("white")
        self.goto(0,280)
        self.hideturtle()
        self.update_scoreboard()
        
    
    #Updation from day24       
   # def game_over(self):
   #     self.goto(0,0)
   #     self.color('white')
   #     self.hideturtle()
   #     self.write("GAME OVER ",align='center',font=('Courier',15,'normal'))
   
    def update_scoreboard(self):
        self.clear()
        self.write(f'Score:{self.score} High Score: {self.highscore}',align='center',font=('Courier','15','normal'))
   
    def reset(self):
        if str(self.score)>(self.highscore):
            (self.highscore)=str(self.score)
            with open("DAY21_data.txt",mode='w') as file:
                file.write(self.highscore)
            #reseting the score
        self.score=0
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()