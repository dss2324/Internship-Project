#docstring are documentation string  that act like  comment & it can be of many line
def formating_name(fname,lname):
    """Take first and last name""" #this is docstring
    if fname=="" or  lname=="":
     return    
    return f"{fname.title()} {lname.title()}"

