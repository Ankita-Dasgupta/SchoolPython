
a = int(input("enter the first number of your calculation "))
b = int(input("enter the second number "))
op=input("Choose your operation by typing +, -,/ or * ")

if op == '+':
    result= a + b
elif op == '-':
    result = a - b
elif op == '/':
    result= round(a / b, 4)
else: result= a * b
print("The answer to your operation is: ", result)
