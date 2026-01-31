a = int(input("Enter your age:"))
#if statment number 1 
if(a%2 == 0):
    print("a is even")
#if statment number 2
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid age")    

elif(a>100):
    print("You too old ")

else:
    print("You are below the age of consent")
    print("Sorry") 

print("End of Program")    