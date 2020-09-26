a=int(input("Enter a number"))
x=int(input("Enter a number to divide with"))
y=int(input("Enter another number to divide with"))
if a%x==0 and a%y==0:
    print("The no. ", a, "is divisible by ", x, "and ",y)
elif a%x==0:
    print("The no. ", a, "is divisible by ", x ,"but not ", y)
elif a%y==0:
    print("The no. ", a, "is divisible by ", y, "but not ", x)
else:
    print("The number is not divisible by either")

 
