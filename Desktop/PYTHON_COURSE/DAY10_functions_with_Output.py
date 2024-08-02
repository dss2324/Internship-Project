
#Function with Output
def format_name(fname,lname):
   return f"{fname.title()} {lname.title()}"
   
output=format_name("dev","dave")
print(output)

#multiple return values
def formating_name(fname,lname):
   if fname=="" or  lname=="":
     return    
   return f"{fname.title()} {lname.title()}"
   
output=format_name("dev","dave")