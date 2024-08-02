#1) Python Primitive Data Types
#a)pulling subscript from string
print("HELLO"[0]);
#integer
print(123+345);
#Float
3.14159;
#Boolean
True;
False;

#2)Type Error ,Type Checking and Type Conversion
#type error is exception that occurs when datatype of an object in an operation is 
#inappropriate
#type() function checks the datatype of variable
print(type(3));
#type conversion
#for type casting 
#we use int()->to convert into integer
#we use float()->to convert into float
#we use str()->to convert into string
age=6;
newage=str(age);
print("your age is "+newage);
a=float(123);
print(70+float("100.5")); #output->170.5
print(str(70)+str(100)); #output->70100
#in same ways all the data type can be converted into each other

#Q1)write a program to add digits of 2 digit numbers
two_digit_number=input("Type a two digit number ");
first_digit=two_digit_number[0];
second_digit=two_digit_number[1];
#here we use type conversion since input recived from input() is string
result=int(first_digit)+int(second_digit);
print(result);

#3)Mathematical Operations in Python
3+5;
3-5;
3*2;
6/3; #in division ans is always float
2**2;#it performs exponential equation ie it work as 2^2
#FOLLOW PEMDAS (Parantheses,Exponents,Multiplication,Division,Addition,Subtraction)

#Q2)Calculate BMI 
weight=input("Enter Your Weight : ");
height=input("Enter Your Height in metres :");
bmi=int(weight)/float(height)**2;
print(int(bmi));

#4)Number Manipulation and F String in Python
#we use round() function to round off number
print(round(8/3));
print(round(8/3,2)); #here ,2 instructs to round it to two decimal places
print(8//3);#this is known as flow division it will give integer number 

#f-string
#in f string you can insert numerical value in {} without converting it into string
score=0;
isWinnig=True;
print(f"Your score is {score},your height is {height},you are winning is {isWinnig}");