
'''Packing and Unpacking a Tuple'''

#Packing
packed_tuple=1,2,3,4
print(packed_tuple)

"""Output: (1, 2, 3, 4)
"""

#Unpacking Tuple
a,b,c,d=packed_tuple
print(a)
print(b)
print(c)
print(d)

'''
Output:
1
2
3
4
'''

#Unpacking with *
numbers_tuple=1,2,3,4,5,6,7,8,9
first,*middle,last=numbers_tuple
print(first)
print(middle)
print(last)

"""
Output:
1
[2, 3, 4, 5, 6, 7, 8]
9
"""
