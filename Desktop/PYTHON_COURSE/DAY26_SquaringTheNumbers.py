#create a new list using list comprehension that contains square of numbers
#numbers=[1,1,2,3,5,8,13,21,34,55]
#square_numbers=[i*i for i in numbers]
#print(square_numbers)

#create a new list using list comprehension that contains only even numbers
#even_numbers=[i for i in numbers if i%2==0]
#print(even_numbers)

#create a common list that contains number  common from file1 and file2
with open("fil1.txt",mode='r') as datafile1:
    contents=datafile1.readlines()
    
content1=[int(i) for i in contents]
print(content1)

with open("file2.txt",mode='r') as datafile2:
    contents=datafile2.readlines()
    
content2=[int(i) for i in contents]
print(content2)



common_list=[i for i in content1 if i in content2 ]
print(common_list)