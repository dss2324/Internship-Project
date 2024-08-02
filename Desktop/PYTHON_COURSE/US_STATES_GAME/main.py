import  turtle
import pandas
screen=turtle.Screen()
screen.title("U.S. States Game")
image="US_STATES_GAME/blank_states_img.gif"
screen.addshape(image)#this method is used to set some gif images  set as background 
turtle.shape(image)
tim=turtle.Turtle()
#getting coordinates of each states 
#def get_mouse_click_coor(x,y):
#     print(x,y)
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop() it is already in csv file

state_data=pandas.read_csv("US_STATES_GAME/50_states.csv")
state_dict=state_data.to_dict()
score=0
while score<=50:
    answer_state=screen.textinput(title=f"{score}/50 States are Correct",prompt="What's another state's name")
    guess=answer_state.title()
    if answer_state=="Exit":
        break
    elif answer_state=="help":
        for i in state_dict["state"]:
            x_cor=state_dict['x'][i] #here we had access the value in state_dict['x'][i]
            y_cor=state_dict['y'][i] #so if state_dict['x'][1]==139 
            #print(x_cor,y_cor)
            tim.hideturtle()
            tim.penup()
            tim.goto(x_cor,y_cor)
            tim.write(state_dict["state"][i],align="left",font=("Arial",10,"normal"))
            
        
    for i in state_dict["state"]:
        if state_dict["state"][i]==guess:
            score=score+1
            x_cor=state_dict['x'][i] #here we had access the value in state_dict['x'][i]
            y_cor=state_dict['y'][i] #so if state_dict['x'][1]==139 
            #print(x_cor,y_cor)
            tim.hideturtle()
            tim.penup()
            tim.goto(x_cor,y_cor)
            tim.write(guess,align="left",font=("Arial",10,"normal"))
            

#states to learn.csv        
        
screen.exitonclick()