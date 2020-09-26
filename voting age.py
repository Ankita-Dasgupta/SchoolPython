age = int(input("Please Enter your Age"))
if age>=18 and age<=100:
    print("you are eligible to vote")
elif age<=0 or age>100:
    print("INVALID")
else: print("you are not eligible to vote")
