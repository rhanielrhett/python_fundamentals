# super module runs with Python 3

# Special methods are defined with underscores. Init is first and most common method when working with classes
# Two more common special methods are repr or str
# The three methods: init, repr and str are the most common ones
class Employee:
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay 
		self.email = first + '.' + last + '@email.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	#repr is meant to be an unambiguous representation of the object and should be used for debugging and logging
	def __repr__(self):
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

	#str is meant to be more of a readable repr of an object. And is used as a display to the end user
	def __str__(self):
		return '{} - {}'.format(self.fullname(), self.email)
		#pass

	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.fullname())

emp_1 = Employee('Alan', 'Preciado', 500)
emp_2 = Employee('Mickey', 'Mouse', 600)

#print(emp_1)

#print(repr(emp_1))	#In the background, it is calling directly those special methods
#print(str(emp_1))

#print(emp_1.__repr__())
#print(emp_1.__str__())

#print(emp_1 + emp_2) #We have defined in the background our custom add operation. Which takes employee objects
#print(3+2)

print(len(emp_1))