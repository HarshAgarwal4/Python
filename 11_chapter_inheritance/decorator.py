class e:
    a = 1
    @classmethod
    def sow(cls):
        print(cls.a)

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self , value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        

a = e()
a.a=45
a.sow()

a.name = "Harsh Agarwal"
print(a.fname,a.lname)
print(a.name)