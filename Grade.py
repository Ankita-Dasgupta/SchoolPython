marks=int(input(" Please Inout Marks for the student : "))
if (marks >=80 and marks <=100):
    print("Grade is A")
elif (marks <=79 and marks >=60):
    print("Grade is B")
elif (marks <=59 and marks >=33):
    print("Grade is C")
elif (marks >=0 and marks <=32):
    print("Grade is F")
else:
    print("Invalid")
