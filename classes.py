class Animal():

    #name = None 
    #age = None
    #voice = None

    def __init__(self, name, age, voice):
        
        self.name = name
        self.voice = voice
        self.age = age
    
    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, value):
        if (value<=0):
            raise ValueError ("Age should be integer")
        self.age = value
            
    def speak(self):
        print(self.voice)

class  Bird(Animal):

    canFly = True
    
    def fly(self):
        if (self.canFly == True):
            print ("I'm flying")
        else:
            print ("I can't fly")

class Fish(Animal):

    canSwim = True

    def speak(self):
        print("-")

    def swim(self):
        if (self.canSwim == True):
            print ("I'm swimming")
        else:
            print ("I can't swim")