a=float(input("Input the temperature: "))
b=int(input("Input:\n1 to convert to Celsius\n2 to convert to Fahrenheit\n"))
if(b==1):
    print(((a-32)*5)/9)
elif(b==2):
   print(((a*9)/5)+32)
else:
   print("Invalid Input")
