#list comprehension
#new_list=[new_item for item in list]
#normal method             Vs                   list comprehension
#numbers=[1,2,3]            |                  numbers=[1,2,3]
#new_list=[]                |                 new_list=[n+1 for n in numbers]
#for n in list:             |
# add_1=n+1                 |               conditional list comprehension
#new_list.append(add_1)     |          new_list=[new_item for item in list if test]
#___________________________|___________________________________________________

#numbers=[1,2,3]
#using list comprehension
#new_number=[n+1 for n in numbers]
#print(new_number)

#create a new list from the range where the list items are double the value in the range
n=range(1,5)
new_list=[number*2 for number in n]
print(new_list)

#create a new list that contains the names longer than 5 character in ALL CAPS
names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
modified_names=[n.upper() for n in names if len(n)>5 ]
print(modified_names)