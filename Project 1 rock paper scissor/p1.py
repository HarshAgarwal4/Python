import random

choices = ['rock' , 'paper' , 'scissor']

print("1. rock\n2. paper\n3. scissor")
a = input("Enter your choice = ")
r = random.choice(choices)
print(a)
if(a != 'rock' and a !='paper' and a !='scissor'): print("enter a valid input")
elif(a == r) : print("Both have same choice")
else:
    if((a == 'rock' and r == 'scissor') or (a=='scissor' and r=='paper') or (a=='paper' and r=='rock')): 
        print("You won")
        print("computer guessed" , r)
    else: 
        print("You lose")
        print("Computer guessed ",r)