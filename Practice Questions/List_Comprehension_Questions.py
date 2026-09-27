'''List Comprehension '''



'''1. Create a new list containing only numbers greater than 15.'''

# import random

# numbers=[random.randint(1,100) for i in range(100)]

# l2=[num for num in numbers if num>15]
# print(l2)

'''2. Even numbers become "Even"
Odd numbers become "Odd"'''

# l2=[f'Even -->{num}' if num%2==0 else f"Odd-->{num}" for num in numbers ]
# print(l2)

'''3. Numbers greater than or equal to 20 become "Pass"
Numbers below 20 become "Fail"'''

# l2=[f'Pass -> {num}' if num>=20 else f"fail -> {num}" for num in numbers]
# print(l2)

'''4. Create a list containing the length of only those words that have more than 5 characters.'''
words = ["apple", "banana", "kiwi", "orange", "grape", "watermelon"]

# l2=[len(word) for word in words if len(word)>5 ]
# print(l2)

'''5. Create a new list using list comprehension where:

If the number is even, store its square
If the number is odd, store its cube '''

# numbers = [5, 12, 7, 20, 3, 18, 25, 10]

# l2=[f'{num} -> {num**2}' if num%2==0 else f'{num} -> {num**3}' for num in numbers]
# print(l2)
