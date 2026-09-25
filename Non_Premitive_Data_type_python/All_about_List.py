
'''1.iterating with index'''

l=[1,2,3,4,5,6,7,8,9,10]
for index,number in enumerate(l):
    print(index,number)

'''
Output
0 1
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10
'''


'''2.List comprehension'''

l=[]
for i in range(10):
    l.append(i**2)
print(l)

'''output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]'''

l1=[i**2 for i in range(10)] # Syntax: [expression for item in iterable]
print(l1)

'''output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]'''



'''3.List comprehension with condition'''

#if even numbers

even=[num for num in range(10) if num%2==0] # Syntax: [expression for item in iterable if condition]
print(even)

'''output: [0, 2, 4, 6, 8]
'''



'''4. List Comprehension with Else'''

odd_or_even=["Even" if num%2==0 else "Odd" for num in l1] #Syntax: [expression_if_true if condition else expression_if_false for item in iterable]
print(odd_or_even)

'''output: ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']'''



'''5. Nested list comprehension'''

list_1=['a','b','c']
list_2=[1,2,3]
pair=[[item_1,item_2]for item_1 in list_1 for item_2 in list_2] #syntax: [expression for item1 in iterable1 for item2 in iterable2]
print(pair)

'''Output : [['a', 1], ['a', 2], ['a', 3], ['b', 1], ['b', 2], ['b', 3], ['c', 1], ['c', 2], ['c', 3]]
'''