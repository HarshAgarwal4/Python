age = int(input("Enter age = "))
if(age >= 18):
    print("Hello")
    print("you are teen")
    print("You can vote")
    print("You can drive")
elif(age<0):
    print("enter a valid age") 
else: 
    print("you are below 18")