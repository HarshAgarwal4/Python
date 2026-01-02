class Employee:
    company="ITC"
    salary = 1000000
    def show(self):
        print(f"salary = {self.salary}")
    
    def __init__(self):
        print("constructor of base class")

class programmer(Employee):
    a=1
    def __init__(self):
        super().__init__()
        print("constructor of child class")

a = Employee()
a = programmer()
a.show()
print(a.company)