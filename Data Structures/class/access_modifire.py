class Employee:
    var=13
    _proctectedVar=8
    __rivetVar=2002
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age

#print(Employee.var)
ob=Employee("sourav","nayek",20)
print(ob.var)
print(ob._proctectedVar)
print(ob._Employee__rivetVar)  #Name Mangaling