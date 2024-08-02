#Functon with input
#def my_function(something): something:-Parameter, Dev:-Argument
# do this "something"
# then do this
# finally do this

#eg
#name=input("enter your name")
#def greet_with_name(name):
#    print(f"hello {name}")
#    print(f"how do you do {name}")
#greet_with_name(name);

#Function with more than 1 input
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
#The following is example of positional argument,here position matters
greet_with("Dev","Rajkot")

#Keyword arguent,here position don't matter (Parameter2=Argument2,Parameter1=Argument1)
greet_with(location="Rajkot",name="Dev");
