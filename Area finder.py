pi= 3.14
print("Enter a number corresponding to the shape whose area you would like to find")
print("(1)Circle")
print("(2)rectangle")
print("(3)Cone")
print("(4)Cube")
print("(5)Triangle")
print("(6)Cylinder")

op=int(input("Enter your number here-> "))
if op==1:
       r=float(input("Enter the radius"))
       print(pi*r**2)
elif op==2:
    l=float(input("Enter the length"))
    b=float(input("Enter the breadth"))
    print(l*b)
elif op==3:
    h=float(input("Enter the slant height"))
    r=float(input("Enter the radius"))
    print(pi*r*(r + h))
elif op==4:
    a=float(input("Enter the side"))
    print(a**3)
elif op==5:
    h=float(input("Enter the height"))
    b=float(input("Enter the base"))
    print(h*b/2)
elif op==6:
    h=float(input("Enter the height"))
    r=float(input("Enter the radius"))
    print(h*r*2*pi)

else:
    print("INVALID OPTION")
