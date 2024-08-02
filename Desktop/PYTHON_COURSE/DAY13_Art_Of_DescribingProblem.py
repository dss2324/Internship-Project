#Debugging Workout
#1)Describe the Problem
#def my_func():
# for i in range(1,20):    #correction:-range(1,21)
#   if i==20:
#     print("you got it")
#my_func()

#2)Reproduce the bug
#from random import randint
#dice_imgs=["|1|","|2|","|3|","|4|","|5|","|6|"]
#dice_num=randint(1,6)    #correction:-randint(0,5) since dice_img is list
#print(dice_imgs[dice_num])

#3)Play computer
#year=int(input("what is your birth year? "))
#if year>1980 and year<1994:
# print("you are millenial")
#elif year>1994:        #correction:-year>=1994:
# print("you are gen z")


#4)Fix the errors
#age=input("how old are you")  #correction:-int(input("how old are you"))
#if age>18:
#  print("you can drive at {age}") #correction:- f" "

#5)Print is your friend
#pages=0
#words_per_pages=0
#pages=int(input("Number of pages: "))
#words_per_page==int(input("Number of words per page")) #correction:-=
#total_words=pages*words_per_page
#print(total_words)

#6)Use a Debugger
#def mutate(a_list):
#  b_list=[]
#  for item in a_list:
#    new_item=item*2
#    b_list.append(new_item)
#   print(b_list)
#mutate([1,2,3,5,8,13])



