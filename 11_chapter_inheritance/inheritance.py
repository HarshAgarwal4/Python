class Employee:
    company="ITC"
    salary = 1000000
    def show(self):
        print(f"salary = {self.salary}")

class programmer(Employee):
    c = 'a'

a = programmer()
a.show()
print(a.company)