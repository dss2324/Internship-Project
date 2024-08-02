#List is a type of Data Structre
fruits=["cherry","apple","pear"]
print(fruits[0]);
print(fruits[-1]); #-1 refer to last item of list
fruits[2]="mango"; #to change item of list
print(fruits[2]);
#adding item to list
fruits.append("grapes"); #it will be on last index
print(fruits[-1]);
fruits.extend(["guava","pineapple","dragonfruit"]) #it will add new list to existing list
print(len(fruits)) #to find size of list
fruits.insert(0,'papaya')#it insert a new item at specified index
print(fruits)
#remove()->remove item from list
fruits.remove("papaya")
print(fruits)
#pop()->remove element at specific index or last item if index is not specified
fruits.pop(0)
print(fruits)
#copy()-> returns a copy of list
newfruits=fruits.copy()
print(newfruits)
#clear()->remove all elements from list
newfruits.clear()
print(newfruits)
#reverse->reverse the order of list
#count->returns number of elements with specified value
fruits.count('guava')#gives index number of guava
#sort()->sorts the list
s=[4,7,2,9,0]
s.sort()
print(s)#->[0,2,4,7,9]


#tuples->similar like list
#tuples are immutable sequence of python objects
#immutable sequence->means once it created no change can be done in it
b=(4,8,10,0)#this is an example of tuple
print(b)
#lists enclosed in [], while tuple enclosed in ()
#count()->returns number of time a specified value occur in tuple
s=[1,1,23,3,4,4,4]
print(s.count(4))
#index()->method searches tuple for a specified value and retrun the position of where it was found
print(s.index(23))
#len()->retrun length of tuple
print(len(s))
#join two tuple using + operators 
s=(1,2,3)
s1=(4,5,6)
s3=s+s1
print(s3)

