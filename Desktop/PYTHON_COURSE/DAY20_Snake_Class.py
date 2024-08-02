#Our Code
#x_pos=[0,-20,-40]
#for square in range(0,3):
#    t=Turtle()
#    t.shape('square')
#    t.color('white')
#   t.goto(x_pos[square],0)



import turtle
from turtle import Turtle, Screen

STARTING_POSITIONS=[(0, 0), (-20, 0), (-40, 0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    import turtle
    from turtle import Turtle, Screen
    

    def __init__(self):
         self.segmentslist=[]
         self.create_snake()
         self.head=self.segmentslist[0]
         
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
                
            
    def add_segment(self,position):
            new_segment = Turtle("square")
            new_segment.color("lightgreen")
            new_segment.penup()
            new_segment.goto(position)
            self.segmentslist.append(new_segment)
            
    def reset(self):
        for seg in self.segmentslist:
            seg.goto(1000,1000)
        self.segmentslist.clear()
        self.create_snake()
        self.head=self.segmentslist[0]
        
                
    def extend(self):
        #add a new segement to snake
        self.add_segment(self.segmentslist[-1].position())        
            
    def move(self):
        #global segmentlist
        for seg_num in range(len(self.segmentslist) - 1, 0, -1):  # indicates indices of segmentlist and decrementting it by one
            new_x = self.segmentslist[seg_num - 1 ].xcor()  # here we take 2nd last segments cordinates
            new_y = self.segmentslist[seg_num - 1 ].ycor()  # then when we move first segment to any position second segment will take place of first segment and third segment will take place of second in this manner it works
            self.segmentslist[seg_num].goto(new_x, new_y)
        # eg:-[3][2][1] when we turn it to left by 90 degrees
        #   [1]
        # [3][2]  notice here how second segment take position of first segment in this manner we interconnect the position and making segments dependent on  it's previous segment
        #
        #self.segmentslist[0].forward(20)  # when we move first segment then only our above process take place
        self.head.forward(20)
        
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
        #self.segmentslist[0].setheading(UP) 
        #we are turning first segment face to 90 deg so that when it faces
        #up and then move upwards
        
    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)
        #self.segmentslist[0].setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        #self.segmentslist[0].setheading(LEFT)
        
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        #self.segmentslist[0].setheading(RIGHT)
        
    