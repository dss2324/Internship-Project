#Class Inheritance
class Animal:
    
    def __init__(self):
        self.num_eyes=2
        
    def breathe(self):
        print("inhale exhale")
        
class Fish(Animal):  #here animal is super class that is getting inherited
    
    def __init__(self):
        super().__init__()  #here when we define constructor of Fish we also call constructor of super class Animal
        
    def swim(self):
        print("moving in water")
        
    def breathe(self):
        super().breathe()     #here we had made breathe function specifically for fish
                            #we have inherited all functionalities from Animal breathe() and also added some sort of our functionalities
        print("doing this in water")
        
    
nemo=Fish()
nemo.swim()
print(nemo.num_eyes)
nemo.breathe()      
    
    
#how to slice lists and tuples