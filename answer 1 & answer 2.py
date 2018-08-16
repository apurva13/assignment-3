#Q1)Create a list with user defined inputs.
#Q2)Add the following list to above created list:
#[‘google’,’apple’,’facebook’,’microsoft’,’tesla’] 
LIST=[]
n=int(input("enter total no. of value:"))
for x in range(n):
    x=input("enter item:")
    LIST.append(x)
print (LIST)

LIST2=['google','apple','facebook','microsoft','tesla']
LIST.extend(LIST2)
print(LIST)
