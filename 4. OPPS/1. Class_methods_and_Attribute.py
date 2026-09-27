
'''1. Instance Variable/Attribute and Methods'''

# Variables/Attribute
class student:

    def __init__(self,Name,Age): # __inti__ is constructor used to define all the initial parameter in a class
        self.Name=Name
        self.Age=Age

student_1=student('yoo',29)
print(student_1.Name,'\n',student_1.Age)

'''Output :
yoo
 29'''

# Methods
class person:

    def __init__(self,name):
        self.name=name

    def Hi (self): # A method name Hi in person class
        print(f"Hi there, my name is {self.name}")

pr1=person("Ago")
pr1.Hi()

'''Output : Hi there, my name is Ago'''



# Example of An BankAccount

class BankAccount():

    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    def check(self):
        print(f"Dear customer {self.name}, your current Balance Amount is {self.balance}")

    def deposit(self,amount):
        self.balance+=amount
        print(f"Dear customer {self.name}, {amount} is added to your account, Your current Balance Amount is {self.balance}")

    def withdraw(self,amount):
        if self.balance<amount:
            print("Your current balance is insufficient to make the withdrawal ")
        else:
            self.balance-=amount
            print(f"Dear customer {self.name}, {amount} is been withdrawer from your account, Your current Balance Amount is {self.balance}")

id_101=BankAccount("Entropy",10000)

id_101.check()
'''Output : Dear customer Entropy, your current Balance Amount is 10000'''

id_101.deposit(5000)
""" Output : Dear customer Entropy, 5000 is added to your account, Your current Balance Amount is 15000 """

id_101.withdraw(105000)
'''Output : Your current balance is insufficient to make the withdrawal '''

id_101.withdraw(10500)
'''Output : Dear customer Entropy, 10500 is been withdrawer from your account, Your current Balance Amount is 4500'''