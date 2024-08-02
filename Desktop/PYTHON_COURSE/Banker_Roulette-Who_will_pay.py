import random
people=int(input("How many people are you folks ?"));
names_string=input("Give me evreybody's name seprated by comma ");
names=names_string.split(",");
#names is list
print(names);
print(f"{names[random.randint(0,people-1)]} is going to buy today's meal ! ");
#if you go beyond index people-1 it will throw index error