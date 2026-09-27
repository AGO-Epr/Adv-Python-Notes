
'''Exception handling : Exception handling in Python allows you to handle errors gracefully and take corrective
                        actions without stopping the execution of the program. This lesson will cover the basics
                        of exceptions, including how to use try, except, else, and finally blocks.

What Are Exceptions?
Exceptions are events that disrupt the normal flow of a program.
They occur when an error is encountered during program execution.

Common exceptions include:

ZeroDivisionError: Dividing by zero.
FileNotFoundError: File not found.
ValueError: Invalid value.
TypeError: Invalid type.'''

# a=b Here as b is not define so it will give an name error

'''Output : py", line 20, in <module>
    a=b  # Here as b is not define so it will give an name error
      ^
NameError: name 'b' is not defined '''

# 1. Exception try and except block
a=10
try:
    a=b
except:
    print("The variable is not define ")
'''Output: The variable is not define '''


# 2. if I know the error

b=10
try:
    b=c
except NameError as er:
    print(er)
''''Output: name 'c' is not defined'''

# 3. Handling multiple exceptions

try:
    div=1/2
    div=u
except ZeroDivisionError as er:
    print(er)
except Exception as er: # Exception is the parent class of all the exceptions as all the Exception are derived from it.
    print(er)
    print('some exception got caught here')

'''Output: name 'u' is not defined
some exception got caught here
'''

'''Another Example'''
# 4. else and finally block
try:
    num=int(input("Enter a number: "))
    div=20/num
except ValueError :
    print("This is not a valid number")
except ZeroDivisionError :
    print(" Given number must be grater then Zero ")
except Exception as er:
    print(er)
else:                              # The else part will only de executed if the try block runs didn't have any error
    print(f"The answer is {div} !")
finally:
    print("End of Code")           # The finally block will compersourly get executed
