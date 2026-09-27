
'''Inheritance : Allows a class to inherit attributes and methods from another class.'''

# Example :

class car():

    def __init__(self,engine_type,fuel,transmission,drive):
        self.engine_type=engine_type
        self.fuel=fuel
        self.transmission=transmission
        self.drive=drive

    def info(self):
        print(f"Your engine Type is {self.engine_type} taking {self.fuel} as a main fuel with {self.transmission} transmission and {self.drive} drive")

car1=car('V-8','petrol','semi-auto','rear wheel')
car1.info()

'''Output : Your engine Type is V-8 taking petrol as a main fuel with semi-auto transmission and rear wheel drive '''

# using another class as tesla and inheriting the class car in it

class Tesla(car):

    def __init__(self,engine_type,fuel,transmission,drive,self_driving):
        super().__init__(engine_type,fuel,transmission,drive)
        self.self_driving=self_driving
        ''' super() keyword is use to call the parent class. In this line the super is calling the init
        from the parent class so we don"t need to define the parameters which are present in the parent class'''

    def selfdriving(self):
        print(f"self driving feature : {self.self_driving}")

ele=Tesla('Electric Motor','Electricity','Automatic','All wheel',True)

ele.selfdriving()
"""Output: self driving feature : True """

ele.info()
'''Output : our engine Type is Electric Motor taking Electricity as a main fuel with Automatic transmission and All wheel drive '''





# MULTIPLE inheritance

class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Subclass must implement this method")

## BAse class 2
class Pet:
    def __init__(self, owner):
        self.owner = owner


##Derived class
class Dog(Animal,Pet):
    def __init__(self,name,owner):
        Animal.__init__(self,name) # Here the super() keyword will not work we have to use the class name and its parameters
        Pet.__init__(self,owner)

    def speak(self):
        return f"{self.name} say woof"


## Create an object
dog=Dog("Buddy","Ago")

print(dog.speak())
'''Output : Buddy say woof'''

print(f"Owner:{dog.owner}")
'''Output : Owner:Ago'''

