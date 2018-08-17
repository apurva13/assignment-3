#Q1)Create a list with user defined inputs.
LIST=[]
n=int(input("enter total no. of value:"))
for x in range(n):
    x=input("enter item:")
    LIST.append(x)
print (LIST)

#Q2)Add the following list to above created list:
#[‘google’,’apple’,’facebook’,’microsoft’,’tesla’] 
LIST2=['google','apple','facebook','microsoft','tesla']
LIST.extend(LIST2)
print(LIST)

#Q3)Count the number of time an object occurs in a list. 
LIST=[]
n=int(input("enter total no. of value:"))
for x in range(n):
    x=input("enter item:")
    LIST.append(x)
object=input("enter value to be counted:")
print("TOTAL NUMBER OF COUNT :",LIST.count(object))

#Q4)create a list with numbers and sort it in ascending order. 
LIST=[]
n=int(input("enter total no. of value:"))
for x in range(n):
    x=int(input("enter item:"))
    LIST.append(x)
LIST.sort()
print("SORTED LIST:",LIST)


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

#Count even and odd numbers in that list.
LIST=[]
n=int(input("enter total no. of value:"))
for x in range(n):
    x=int(input("enter numbers:"))
    LIST.append(x)
even=0
odd=0
for j in LIST:
    if j%2==0:
        even+=1
    else:
        odd+=1
print('Total even numbers:',even)
print('Total odd numbers:',odd)

#Implement a stack and queue using lists.
stack=['Sheenam','Apurva','Yashika']
print('Stack:',stack)
stack.append('Aparna')
print('Updated Stack:',stack)
stack.append('Niharika')
print('Updated Stack:',stack)
stack.pop()
print('Updated Stack:',stack)
stack.pop()
print('Updated Stack:',stack)
print()
#Stack is Last In First Out (LIFO) in this element is added to the last of list
# and deletion also starts from the last element of list

queue=['Sheenam','Apurva','Yashika']
print('Queue:',queue)
queue.append('Aparna')
print('Updated Queue:',queue)
queue.append('Niharika')
print('Updated Queue:',queue)
queue.pop(0)
print('Updated Queue:',queue)
queue.pop(0)
print('Updated Queue:',queue)
#Queue is Firts In First Out(FIFO) in this element is added to the last of list
#but deletion starts from the first element of list




