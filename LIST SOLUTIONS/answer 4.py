#create a list with numbers and sort it in ascending order. 
LIST=[]
n=int(input("enter total no. of value:"))
for x in range(n):
    x=int(input("enter item:"))
    LIST.append(x)
LIST.sort()
print("SORTED LIST:",LIST)
