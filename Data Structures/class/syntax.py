class Employee:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age

sourav= Employee('sourav', 'nayek', 20)
saikat= Employee('saikat', 'nayek', 28)

print(sourav.fname,saikat.age,sep='\n')