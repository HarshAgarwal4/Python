class Employee:
    language = 'py'
    salary = '2400000'
    def getInfo(self):
        print(f"salary is {self.salary}\nlanguage is {self.language}")
    
    # def greet(self):
    #     print("Good morning")

    @staticmethod
    def greet():
        print("Good morning")

harsh = Employee()
harsh.getInfo()
harsh.greet()
