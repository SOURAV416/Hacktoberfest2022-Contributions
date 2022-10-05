class Car:
	def __init__(self, carname):
		self.__make = carname
	
	def set_make(self, carname):        # Defining Mutator Method
		self.__make = carname
	
	def get_make(self):                 # Defining Accessor Method
		return self.__make
myCar = Car('Ford')

print (myCar.get_make())                #Ford
myCar.set_make('Porche')
print (myCar.get_make())                #Porche

##So, here the name of the car was accessed using Accessor method 
#i.e, get_make and then it was modified using Mutator method i.e, set_make.
