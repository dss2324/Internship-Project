#for loops
#syntax:-for item in list_of_items:
#        do something to each item
fruits=["Apple","Peach","pear"];
for fruit in fruits:
    print(fruit);#here variable fruit is same as variable i of java & c++ 
    print(fruit+"pie");
#BELOW LINE IS NOT PART OF FOR LOOP    
print(fruits);
        
#Q1)Calculate average student height from given list
student_heights=input("input a list of students height ").split(",");
#to convert string of list into integer list
for j in range(0,len(student_heights)):
    student_heights[j]=int(student_heights[j]);
print(student_heights);
#here actual process starts
sum,avg=0,0;
for i in student_heights:
    sum=sum+i;
avg=int(sum/len(student_heights));
print(f"Average height from given heights are {avg}");

#Q2)Calculate highest score from given list of score
student_score=input("Enter scores of students").split(",");
#to convert string list into integer list
for j in range(0,len(student_score)):
    student_score[j]=int(student_score[j]);
print(student_score)
#calculation of highest score
max=0;
for i in student_score:
    if(max<i):
        max=i;
print(f"Maximum Score From List is {max}");
    
#range() function -> for number in range(a,b)
#EG:- 
#for n in range(1,10): #here last no of range will not be included 
    #print(n)
#Q3) Calculate sum of all even number btw 1-100 including 1 & 100
sum=0;
for i in range(1,101):
    if(i%2==0):
        sum=sum+i;
print(f"Sum of all even number is {sum}");

#Fizz Buzz problem
#your program should print each no from 1 to 100 in  turn ,when number is divisible by 3
#then instead of printing into no it should print "Fizz" ,when number divisible 5,then instead
#of printing no it should print "Buzz", & if no is divisible by both  3&5 it should print FizzBuzz
for i in range(1,101):
    if(i%3==0 and i%5==0):
        print("FizzBuzz");
    elif(i%3==0):
        print("Fizz");
    elif(i%5==0):
        print("Buzz");
    else:
        print(i);
        