
'''1. Lambda Functions'''
# Syntax lambda arguments: expression

addition=lambda a,b:a+b
print(addition(2,3))

'''Output: 5'''

even=lambda a:a%2==0
print(even(100))

'''Output : True'''




'''2. Map() function'''

'''The map() function applies a given function to all items in an input list
(or any other iterable) and returns a map object (an iterator).
This is particularly useful for transforming data in a list comprehensively.'''

def square(num):
    return num**2

list_num=[1,2,3,4,5,6,7,8,9,10]

list_sq_num=list(map(square,list_num))
print(list_sq_num)

'''Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]'''




'''3. Lambda with map()'''

print(list(map(lambda x:x**2,list_num)))

'''Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]'''




'''4. Map() with Multiple iterable '''

num_1=[1,2,3,4,5,6,7]
num_2=[8,9,10,11,12,13,14]

print(list(map(lambda x,y:x+y,num_1,num_2))) # Syntax: map( function to implement , The iterable )

'''Output: [9, 11, 13, 15, 17, 19, 21]'''




'''Convert string to int '''
string_num=['1','2','3','4','5']

print(list(map(int,string_num)))

'''Output: [1, 2, 3, 4, 5] '''




""" Applying function in Map() """
word=['hi','bye','Apple','human','world']
print(list(map(str.upper,word)))

'''Output: ['HI', 'BYE', 'APPLE', 'HUMAN', 'WORLD'] '''



'''Using map to get all the Name in the nested dict inside list'''
def get_name(person):
    return person.get('name')

people=[{'name':"Ago_01","Age":20},
        {'name':"Eor","Age":24},
        {'name':"Get-@","Age":26},
        {'name':"yoo_23@#","Age":30}]

print(list(map(get_name,people)))

'''Output: ['Ago_01', 'Eor', 'Get-@', 'yoo_23@#']'''





'''5. filter() function '''
'''It is used to filter out items from a list (or any other iterable) based on a condition.'''



'''Applying filter() on a function'''
def even(num):
    return num%2==0
number=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(even,number)))

'''Output : [2, 4, 6, 8, 10]'''



'''Applying filter with lambda() function'''
print(list(filter(lambda x:x%2==0,number)))

'''Output : [2, 4, 6, 8, 10] '''

"""Applying filter with lambda() and multiple condition"""



# Checking for even and Grater then 5

num_list=[1,2,3,4,5,6,7,8,9,10,123,244,44,54,56,89,91]
print(list(filter(lambda x:x>5 and x%2==0,num_list)))

'''Output: [6, 8, 10, 244, 44, 54, 56]'''
