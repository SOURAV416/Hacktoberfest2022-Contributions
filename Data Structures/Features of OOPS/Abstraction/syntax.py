# Python program showing implementation of abstract
# class through subclassing
import abc
class parent:	
	def git(self):
		pass
class child(parent):
	def git(self):
		print("child class")

print( issubclass(child, parent))
print( isinstance(child(), parent))
