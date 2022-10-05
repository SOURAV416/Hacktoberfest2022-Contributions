def product(a, b):
	p = a * b
	print(p)
	
def product(a, b, c):
	p = a * b*c
	print(p)

# Uncommenting the below line shows an error	
#product(4, 5)

# This line will call the second product method
product(4, 5, 5)

##In the above code, we have defined two product method, but we can only use the second product method, as python does not support method overloading. We may define many methods of the same name and different arguments, but we can only use the latest defined method. Calling the other method will produce an error.