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



'''Dict Comprehension '''



'''{1: 1, 2: 4, 3: 9, ...}'''

# d={i:i**2 for i in range(10)}
# print(d)

'''1. Create a dictionary containing only numbers greater than 20, where:

key = number
value = number × 2'''

# numbers = [10, 15, 20, 25, 30, 35, 40]

# d={num:num*2 for num in numbers if num>20}
# print(d)

'''2. Create a dictionary where:

key = word
value = length of the word'''

# words = ["python", "java", "javascript", "C", "kotlin"]

# d={word:len(word) for word in words}
# print(d)

'''3. Create a dictionary where:

key = number
value = "Even" if the number is even
value = "Odd" if the number is odd'''

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# d={num:"Even" if num%2==0 else "Odd" for num in numbers}
# print(d)

'''4. Create a new dictionary containing only products costing more than ₹40, with the price increased by 10%.'''
# prices = {
#     "apple": 50,
#     "banana": 20,
#     "mango": 80,
#     "orange": 40,
#     "grapes": 100
# }

# new_prices={key:value+int(value*0.1) for key,value in prices.items() if value>40}
# print(new_prices)

'''5. Create a dictionary where:

key = number
If number is even → value = square
If number is odd → value = cube'''

# numbers = [5, 12, 7, 20, 3, 18, 25, 10]

# d={num:num**2 if num%2==0 else num**3  for num in numbers}

# print(d)