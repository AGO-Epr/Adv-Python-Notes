
''' Encapsulation :  Encapsulation involves bundling data and methods that operate on the data within a single unit
                    the concept of wrapping data (variables) and methods (functions) together as a single unit.
                    It restricts direct access to some of the object's components, which is a means of preventing
                    accidental interference and misuse of the data.'''




''' 1. Public variable or access modifiers : Can be access outside the class '''

class student:
    def __init__(self,name,age):
        self.name=name # Public variable
        self.age=age

obj=student("mouse",26)
print(obj.name)
'''Output : mouse'''




''' 2. Private variable or access modifiers : Can't be access outside the class '''

class person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

obj1=person("Key",24)
print(obj1.__name)
'''Output : AttributeError: 'person' object has no attribute 'name''' # As the name and age variable are private so can't be accessed out the class




''' 3. Protected variable or access modifiers : Can't be access outside the Main class but cqn be access through a Derived class'''

class human:
    def __init__(self,name,age):
        self._name=name
        self._age=age

class male(human):
    def __init__(self, name, age):
        super().__init__(name, age)

obj2=human("Ket",56)
print(obj2.name)
'''Output : AttributeError: 'person' object has no attribute 'name'''

obj2=male('ket',24)
print(obj2._name)
'''Output : ket'''



''' 4. Encapsulation with Getter and Settecr '''

class animal():
    def __init__(self,name,age):
        self.__name=name # Private access modifier
        self.__age=age # Private access modifier

    # Getter method for name
    def get_name(self): # Getter method to get name variable from the class
        return self.__name

    # Setter method for name
    def set_name(self,name): # Setter method to set or change the name in the class
        self.__name=name

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method for age
    def set_age(self,age):
        if age>=0:
            self.__age=age
        else:
            print("Can't accept negative age ..!")

dog=animal("BOB",5)

print(dog.get_name())
'''Output : BOB'''

dog.set_name("TOM") # Now thw name is changed to TOM
print(dog.get_name())
'''Output : TOM '''

print(dog.get_age())
'''Output : 5 '''

dog.set_age(-3)
'''Output : Can't accept negative age ..!'''

dog.set_age(10) # Now thw age is changed to 10
print(dog.get_age())
'''Output : 10'''
