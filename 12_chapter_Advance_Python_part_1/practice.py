# try:
#     with open("Table1.txt") as f1:
#         print(f1.read())
# except Exception as e:
#     print(e)
# try:
#     with open("Table2.txt") as f1:
#         print(f1.read())
# except Exception as e:
#     print(e)
# try:
#     with open("Table3.txt") as f1:
#         print(f1.read())
# except Exception as e:
#     print(e)

# list = [1,2,3,4,5,6,7,8,9,10]

# for i,item in enumerate(list):
#     if(i == 2 or i==4 or i==6):
#         print(item)

# n : int = int(input("Enter a number = "))
# table = [n*i for i in range(1,11)]
# print(table)

# a=int(input("Enter a = "))
# b=int(input("Enter b = "))
# try:
#     print(a/b)
# except ZeroDivisionError as z:
#     print("Infinite")

n : int = int(input("Enter a number = "))
table = [n*i for i in range(1,11)]
print(table)

with open("Tables.txt" , "a") as f:
    f.write("Table of "+ str(n) +" : "+str(table)+"\n")

