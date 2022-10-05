class Employee:
    no_of_siblings=3
    def __init__(self,afname,alname,aage):
        self.fname=afname
        self.lname=alname
        self.age=aage

ob=Employee("sourav", "nayek", 20)  #constructor
print(ob.age)