# class Two_D:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
    
#     def show2DVector(self):
#         print(f"{self.x}i + {self.y}j")

# class three_D(Two_D):
#     def __init__(self, x, y, z):
#         self.z = z
#         super().__init__(x, y)

#     def show3DVector(self):
#         print(f"{self.x}i + {self.y}j + {self.z}k")

#     def __add__(self ,num):
#         return f"{self.x+num.x}i + {self.y+num.y}j + {self.z+num.z}k"

# a = three_D(1,2,3)
# # a.show2DVector()
# a.show3DVector()
# b = three_D(4,5,6)
# b.show3DVector()
# print(a+b)

# class Animals:
#     def __init__(self):
#         print("I am animal")
    
#     def walk(self):
#         print("I can walk")

# class Pets(Animals):
#     def __init__(self):
#         super().__init__()
#         print("I am a pet")

# class Dog(Pets):
#     def __init__(self):
#         super().__init__()
#         print("I am Dog")
    
#     def bark(self):
#         print("I am Barking")

# d = Dog()
# d.bark()

# class Employee:
#     salary = 200
#     increment = 20
#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary + (self.salary*(self.increment/100)))
    
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self , salary):
#         self.increment = ((salary/self.salary) - 1)*100

# a = Employee()
# print(a.increment)
# print(a.salaryAfterIncrement)
# a.salaryAfterIncrement = 280.0
# print(a.increment)
# print(a.salaryAfterIncrement)

class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i

    def __str__(self):
        return f"{self.r} + {self.i}i"

    def __add__(self, c2):
        return str(Complex(self.r+c2.r , self.i+c2.i))
    
    def __mul__(self, c2):
        return str(Complex((self.r*c2.r)-(self.i*c2.i) , (self.r*c2.i)+(self.i*c2.r)))

c1 = Complex(1,2)
c2 = Complex(3,4)
print(str(c1))
print(str(c2))
print(c1+c2)
print(c1*c2)