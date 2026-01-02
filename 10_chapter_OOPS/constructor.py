class Employee:
    language = 'py'
    salary = '2400000'
    name=''

    def __init__(self,name):           # dunder method - thar start with double under score __
        print("constructor is running")   
        self.name = name

    def getInfo(self):
        print(f"name is {self.name}\nsalary is {self.salary}\nlanguage is {self.language}")
    
    # def greet(self):
    #     print("Good morning")

    @staticmethod
    def greet():
        print("Good morning")

harsh = Employee("Harsh")
harsh.getInfo()
harsh.greet()
