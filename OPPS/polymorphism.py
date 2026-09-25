
'''1. Polymorphism : Allows objects of different classes to be treated as objects of a common superclass.
                  It provides a way to perform a single action in different forms. Polymorphism is
                  typically achieved through method overriding and interfaces'''

'''2. Method Overriding
                    Method overriding allows a child class to provide a specific implementation of a
                    method that is already defined in its parent class.'''

# Example :
class Animal():
    def speak(self):
        return ("Sound made by an Animal")
class Dog(Animal):
    def speak(self):
        return ("Wofffff...!!")
class Cat(Animal):
    def speak(self):
        return ("Meowwww...!")

a=Cat()
print(a.speak())

"""Output : Meowwww...! """




'''3. Polymorphism with function and methods '''

class Shape():
    def area(self):
        return "The area of the shape"

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return f"Area of the Rectangle is {self.height*self.width} "

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return f"Area of the Circle is {3.14*self.radius**2} "

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return f"Area of the Triangle is {0.5*self.height*self.base} "

def area_0f_shape(shape): # Creating a function which will take parameter as obj and will call the area function
    print(shape.area())
obj=Rectangle(3,4)
area_0f_shape(obj)
'''Output : Area of the Rectangle is 12  '''

obj=Circle(3)
area_0f_shape(obj)
'''Output : Area of the Circle is 28.26 '''

obj=Triangle(4,6)
area_0f_shape(obj)
'''Output : Area of the Triangle is 12.0 '''




'''4. Method overriding with ABC's'''

'''Abstract Base Classes (ABCs) are used to define common methods for a group of related objects.
They can enforce that derived classes implement particular methods, promoting consistency across different implementations.'''

import abc

class Vehicle(abc):
    @abc.abstractmethod
    def start_engine(self):
        pass

class Car(ValueError):
    def start_engine(self):
        return "Car engine "

class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine"

