#LocalScope Vs GlobalScope
#there is no block scope  in python
#Eg:-if you create a variable when in function then it is only ascessible within function
#but if you create variable in if statements ,for,while loops,switches etc then it is acssebiloe outside that block

#how to modify global variable
enemy=1
eneimies=1
def increase_enemies():
    #enemies=3
    #taking global variable
   # global eneimies
    #eneimies += 1
   # enemy=2
    x=2+enemy
    print(f"enemies inside function : {x}") #will print 2

increase_enemies()
print(f"enemies outside function : {enemy}")#will print 1
#constants and global scope ->Global Constants
#python genrally use uppercase letters to declare global scope 
#eg:-PI=3.14

