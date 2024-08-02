#Creating Classes
class User:
    #self is actual object that is being created or intialised
    #and besides self we can add as many parameters we wish 
    def __init__(self,userid,username):
        self.userid=userid
        self.username=username
        self.followers=0#here we have given default value to follower attribute
        self.following=0
        #print("new user being created")#when you want to create empty class pass keyword is used 
    def follow(self, user):
        user.followers += 1
        self.following += 1
            
#user1=User()
#adding an attribute
#attribute is variable that is associated with object 
#user1.id='007'
#user1.username='Dev'
#print(user1.username)
user=User(123, 'Dev')
user_1=User(234, 'Harshit')
user.follow(user_1)
print(user.followers)
print(user.following)
print(user_1.followers)
print(user_1.following)
print(user.username)
print(user.followers)
#Constructor
#Constructor are created using __init__ function it is used to intialise attributes

