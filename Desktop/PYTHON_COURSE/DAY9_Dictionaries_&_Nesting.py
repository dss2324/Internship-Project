#dictionary is an unordered collection of data values used to store data value like maps i.e 
#dictionary holds the key:value pair 
#1) value in the dictionary can be of any data type and can repeat
#2) the keys in dictionary must be of immutable type (str,int,tuple etc) and must be unique
#are written in {} brackets
programming_dictionary={
    "Bug":"an error in program",
    "Function":"a block of code",
    }

#to fetch value out  of dictionary we use it's key
print(programming_dictionary["Bug"])

#adding new item to dictionary
programming_dictionary["Loop"]="doing something repetitively"

print(programming_dictionary)

#empt dictionary
emp_dictionary={}

#wipe an existing dictinary
#programming_dictionary={}
#print(programming_dictionary)

#Edit an item in dictionary
programming_dictionary["Bug"]="an error that prevent program from executing coorectly"
#in case below it will create a new key list & it's value
programming_dictionary["List"]="an array of same thing"
print(programming_dictionary)

#Loop through dictionary
for key in programming_dictionary:
    print(key) #will give key
    print(programming_dictionary[key]) #will give value
    
    
    
#Nesting 
#{  
#   key:[list],
#   key2:{Dict},
#}
#Nesting List in Dictionary
travel_log={
            "France":["Paris","lille","dijon"],
            "Germany":["berlin","hamburg","stugart"],
                      }
#Nesting Dictionary in Dictionary
travel_log={
          "France":{"cities_visited":["paris","lille","dijon"],"total_visits":12},
        "Germany":{"cities_visited":["berlin","hamburg","stugart"],"total_visits":5},
               }

#Nesting Dictionary in List
travel_log=[
    
{"country":"France",
  "total_visits":12,
 "cities_visited":["paris","lille","dijon"],
 
 },
{"country":"Germany",
  "total_visits":5,
 "cities_visited":["berlin","hamburg","stugart"],
 
 },
    
]

#Add new country to list of travel log
#here you can't add new dictionary to travel_log directly.you need to create a function to modify it
def add_new_country(country_visited,times_visited,cities_visited):
    new_country={}
    new_country["country"]=country_visited
    new_country["total_visits"]=times_visited
    new_country["cities_visited"]=cities_visited
    #adding new dictionary to travel log
    travel_log.append(new_country)
    
add_new_country("Russia",2,["Moscow","Saint Petersburg"])    
print(travel_log)