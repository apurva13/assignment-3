#Q3)Count the number of time an object occurs in a list. 
LIST=[]
n=int(input("enter total no. of value:"))
for x in range(n):
    x=input("enter item:")
    LIST.append(x)
object=input("enter value to be counted:")
print("TOTAL NUMBER OF COUNT :",LIST.count(object))
