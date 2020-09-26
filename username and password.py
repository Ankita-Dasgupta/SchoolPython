a = "USER"
b = "PASS"
username= input("Enter the username: ")
if username == a:
    print("Username accepted")
    password = input("Enter the password: ")
    if password==b:
          print("password accepted")
          print("you have successfully logged in")
    else:
          print("password is incorrect")
else:
    print("username is incorrect")
