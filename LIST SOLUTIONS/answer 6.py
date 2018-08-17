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
