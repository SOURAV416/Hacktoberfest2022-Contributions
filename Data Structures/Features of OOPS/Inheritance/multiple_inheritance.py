# Python program to demonstrate multiple inheritance

# Base class1
class Mother:
	mothername = ""
	def mother(self):
		print(self.mothername)

# Base class2
class Father:
	fathername = ""
	def father(self):
		print(self.fathername)

class Son(Mother, Father):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)

s1 = Son()
s1.fathername = "Errol"
s1.mothername = "Maye"
s1.parents()
