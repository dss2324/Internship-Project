#comparision operators-> ==,!=,>=,<=
print(10>=7)
#logical and-> when both of them are true gives 2nd value
print(8 and 81)
#logical or->when both of them are true gives 1st value
print(11 or 10)
#logical not->it shows inverse of the input
print(not 11)
#bitwise &
print(11 & 10)
#bitwise |
print(11|3)
#bitwise ~
print(~11)
#identity operators
#is operator-> it compare values of two variables
x,y=10,10
print(x is y)
#is not operator-> inverse of is operator
x,y=10,12
print(x is not y)
#membership operators->used to validate the membership of a value
#in operator->evaluate true if it find a variable in specified sequence & false otherwise
t=(1,2,3,4)
print(3 in t)
#not in->inverse of in
t=(1,2,3,4)
print(2 not in t)
#different string methods
#captalized()->convert 1st letter to capital
s='bollywood'
print(s.capitalize())
#lower()->converts all character to lower case
s='hollywooD'
print(s.lower())
#upper()->converts all character to upper case
s='darshana'
print(s.upper())
#join()->return the string after concatenating elements of the string with a separator
s=['ram','shyam','mohan']
x=" ".join(s)
print(x)
#len()->count length of string
s='darshana'
print(len(s))
#count()->return no. of occurence of substring
s='darshana'
print(s.count('a'))
#find()->returns the index of substring if it is found, else returns -1
s='dev'
print(s.find('c'))
#is lower()->check if all are lower or not
s='chakku masi'
print(s.islower())
#is upper()->inverse of is lower()
s='dev'
print(s.isupper())
#split()->returns a list of string after breaking the string by separator
s='darshana dave'
print(s.split('a'))
#strip()->remove extra spaces from begining and end
s='   dev dagli  '
print(s.strip())

