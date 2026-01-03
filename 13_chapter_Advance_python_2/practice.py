# name=input("Enter name = ")
# marks = int(input("Enter marks = "))
# phone = int(input("Enter phone number = "))

# print("The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,phone))

# l=[1,2,3,4,5,6]
# list = [i for i in l if i>3]
# print(list)
# list = [str(7*i) for i in range(1,11)]
# print(list)
# print('\n'.join(list))

# list1 = [5,10,11,15,42,36]
# def divisible(n):
#     if(n%5==0): return True
#     else: return False

# print(list(filter( divisible , list1)))

from functools import reduce
l = [1,2,4,34,5,6,5]
g = lambda a,b : a if(a > b) else b

print(reduce(g,l))