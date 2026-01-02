import random

score = 0
computer = random.randint(1,101)

while(True):
    n = int(input("Enter number = "))
    if(n not in range(1,100)):
        print("Enter in valid range 1 to 100")
    elif(n < computer): 
        print("Higher number please")
        score+=1
    elif(n > computer): 
        print("Lower number please")
        score+=1
    else:
        score+=1
        print(f"Congrats!! you guessed correct number {n} in {score} attempts")
        break