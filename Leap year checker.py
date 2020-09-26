y=int(input("Enter the year"))

#check if y is divisible by 4
if y%4 == 0:
    #if y is divisible by 4 , check if y is divisible by both 100 and 4
    
    if y%100==0:
      #if y is divisible by 4 and 100, check if y is divisible by 400
      
        if y%400==0:
        #if y is divisible by 400, 4 and 100 we say its a leap year
            print("The year ", y, "is a leap year")
        
        else:
            # if y is divisible by 4 and 100 but not by 400 it is not a leap year
            print("The year " , y, "is not a leap year")
          
       
    else:
        # if y is only divisible by 4 and not 100
        print("The year ", y, "is a leap year")
    
#if y is not divisible by 4 it is not a leap year
else:
    print("The year ", y, "is not a leap year")
