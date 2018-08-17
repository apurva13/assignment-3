"""
Q5)Given are two one-dimensional arrays A and B which are sorted in ascending 
order.Write a program to merge them into a single sorted array C that contains
every item from arrays A and B, in ascending order. [List] 
"""
A=[]
B=[]
n=int(input("enter total no. of value in list A:"))
for x in range(n):
    x=int(input("enter item:"))
    A.append(x)
n2=int(input("enter total no. of value in list B:"))
for x in range(n2):
    x=int(input("enter item:"))
    B.append(x)
A.sort()
B.sort()
print("SORTED LIST A:",A)
print("SORTED LIST B:",B)
A.extend(B)
A.sort()
C=A
print('MERGED SORTED LIST :',C)

