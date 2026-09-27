import random


'''1. Create a Dict'''

Dict=dict() #Empty



"""2. Accessing Elements using get()"""

student={"first_Name":"Priyanshu","Age":20,"last_Name":"Rawat"}
print(student.get("first_Name"))
print(student.get("Address"))

"""
Output:
Priyanshu
None          NOTE: by using get if the key is not available the compiler didn't rase an Error
"""



'''3. Updating, Adding and Deleting Elements'''

dict1={"first_Name":"Priyanshu","Age":20,"last_Name":"Rawat"}
print(dict1)

"""Output: {'first_Name': 'Priyanshu', 'Age': 20, 'last_Name': 'Rawat'}"""

dict1["Age"]=21 # Updating the Age to 21

"""Output: {'first_Name': 'Priyanshu', 'Age': 21, 'last_Name': 'Rawat'}"""

dict1["Hobbies"]="Chilling Out!" # Adding a new key as "Hobbies"

"""Output : {'first_Name': 'Priyanshu', 'Age': 21, 'last_Name': 'Rawat', 'Hobbies': 'Chilling Out!'}"""

del dict1['last_Name'] # The del function deletes the particular key and its values

'''Output: {'first_Name': 'Priyanshu', 'Age': 21, 'Hobbies': 'Chilling Out!'}'''



'''4. Shallow copy'''

student_1={'first_Name': 'Priyanshu', 'Age': 21, 'Hobbies': 'Chilling Out!'}
student_copy=student_1.copy() # copy() id use to make a shallow copy
print(student_1,"\n",student_copy)

'''Output:
{'first_Name': 'Priyanshu', 'Age': 21, 'Hobbies': 'Chilling Out!'}
{'first_Name': 'Priyanshu', 'Age': 21, 'Hobbies': 'Chilling Out!}'''

student_1["first_Name"]="AGO" # Note : this change will not effect the student_copy dict
print(student_1,"\n",student_copy)

"""Output :
{'first_Name': 'AGO', 'Age': 21, 'Hobbies': 'Chilling Out!'}
{'first_Name': 'Priyanshu', 'Age': 21, 'Hobbies': 'Chilling Out!'}"""



'''5. Dict Comprehension'''

square={i:i**2 for i in range(10)}
print(square)
'''Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81} '''

squ_even={i:i**2 for i in range(10) if i%2==0}
print(squ_even)
'''output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64} '''

# Below is a list of 100 random number from 1 to 10 the tasks to to finds each count using dict comprehension
random_num=[ random.randint(0,10) for i in range(100)]

count_dict={i:random_num.count(i) for i in range(11)}
print(count_dict)

'''Output: {0: 6, 1: 15, 2: 9, 3: 9, 4: 11, 5: 10, 6: 8, 7: 10, 8: 9, 9: 5, 10: 8} '''



'''6. Marge Two Dict '''

dict_1={'a':1,'b':2,'c':3}
dict_2={'c':4,'d':5,'e':6}

marge_Dict={**dict_1,**dict_2} # Note ** is an keyword argument used for key:value pair
print(marge_Dict)


'''Output : {'a': 1, 'b': 2, 'c': 4, 'd': 5, 'e': 6}'''