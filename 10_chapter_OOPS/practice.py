# class programmer:
#     name = ''
#     language = ''
#     salary = 0

#     def __init__(self,name,language,salary):
#         self.name = name
#         self.language = language
#         self.salary = salary
#         print(f"name = {name}\nlanguage = {language}\nsalary = {salary}")

# n = int(input("Enter number of employee = "))
# a=[]
# for i in range(0,n):
#     a.append(programmer(input("Enter name = ") , input("Enter language = ") , int(input("Enter salary = "))))

# print(a)

# class calculator:
#     @staticmethod
#     def square(n):
#         print(n**2)
#     @staticmethod
#     def cube(n):
#         print(n**3)
#     @staticmethod
#     def squareRoot(n):
#         print(n**0.5)

# a = calculator()
# a.square(4)
# a.cube(4)
# a.squareRoot(4)

# class Train:
#     ticketCount = 1000
#     name = ''
#     passengers = []

#     def __init__(self , name , count , fare):
#         self.name = name
#         self.ticketCount = count
#         self.fare = fare
    
#     def bookTicket(self ,name , fro , to ):
#         if(self.ticketCount > 0):
#             self.ticketCount = self.ticketCount-1
#             p1 = {
#                 'name' : name,
#                 'from' : fro,
#                 'to' : to
#             }
#             self.passengers.append(p1)
#             print(self.passengers)
#         else:
#             print("No ticket available")

#     def getStatus(self):
#         print("No. of available seats =" , self.ticketCount)
#         print("List of passengers is:-\n" , self.passengers)
    
#     def getFareInfo(self):
#         print("Fare is =",self.fare)

# rajdhani = Train("Rajdhani express" , 500 , 500)
# n=int(input("Enter no of passengers = "))
# for i in range(0,n):
#     rajdhani.getFareInfo()
#     rajdhani.bookTicket(input("Enter name = ") , input("Enter from = "), input("Enter to = "))

# rajdhani.getStatus()