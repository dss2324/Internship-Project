#dictionary is an unordered collection of data values used to store data value like maps i.e 
#dictionary holds the key:value pair 
#1) value in the dictionary can be of any data type and can repeat
#2) the keys in dictionary must be of immutable type (str,int,tuple etc) and must be unique
#are written in {} brackets
d={'brand':'ford','model':'mustang','year':1964}
print(d)
#dict()->another way to write a dictionary
#note->keys are not string litreals i.e. write keys without quotes
#note2->using = rather than :
thisdict=dict(brand="ford",model="mustang",year=1964)
print(thisdict)
#get()->access item from dictionary
print(d.get('brand'))
#adding a new item
d['color']='red'
print(d)

#operations on dictionaries
#copy()->returns copy of dictionaries
d2=d.copy()
print(d2)
#item()->return a list containing a tuple for each key value pair
print(d.items())
#keys()->method which retrun list containing the dictionary keys
print(d.keys())
#pop()->remove elements with specify keys
#print(d.pop(1))
#popitem()removes the last inserted key value pairs
print(d.popitem())
#update()->update the dictionary with specify key value pair
d1={'p1':'harshit','p2':'dev'}
d1.update({'p3':'darshana'})
print(d1);
#clear()->removes all elements from dictionary
d1.clear();
print(d1);
#values()->return a list of all values in the dictionary
dict1={1:"dev",2:"darshana",3:"harshit"}
print(dict1.values())

#Nested Dictionaries-> dictionary inside  dictionary
#nested_dic={dict1:{key1:value1},dict2:{key2:value2}}
student_marks={'Ram':{"maths":75,"science":80,"english":78},
               'Shyam':{"maths":60,"science":65,"english":70},                                          
                'Mohan':{"maths":80,"science":50,"english":68} }
print(student_marks);
print(student_marks['Mohan'])
print(student_marks['Mohan']['maths']);
#adding item to dictionary

student_marks["Rohan"]={}
student_marks["Rohan"]["maths"]=791


student_marks["Rohan"]["science"]=79
student_marks["Rohan"]["english"]=79

