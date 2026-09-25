
'''Abstraction : Abstraction is the concept of hiding the complex implementation details
                 and showing only the necessary features of an object. This helps in
                 reducing programming complexity and effort.'''


from abc import ABC,abstractmethod

# Abstract  Main Class

class animal(ABC):

    @abstractmethod
    def speak(self): # showing only the necessary features of an object
        pass

class dog(animal):
    def speak(self): # Hiding the complex implementation details from Main class
        print("Woooff...!!")

obj=dog()
obj.speak()
'''Output : Woooff...!!! '''