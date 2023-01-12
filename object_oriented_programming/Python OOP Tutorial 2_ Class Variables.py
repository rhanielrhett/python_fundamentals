# Python object-oriented programming
# Tutorials by Corey Schafer: https://www.youtube.com/watch?v=BJ-VvGyQxho

# To understand: Difference between instance and class variables

class Employee:

	#Class variable
	raise_amount = 1.04 #this is an attribute to every instance of Employee

	num_of_emps = 0

	def __init__(self, first, last, pay):

		self.first = first
		self.last = last
		self.pay = pay
		self.email  = first + '.' + last + '@company.com'

		Employee.num_of_emps += 1 #Adds one each time an instance of Employee is created

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def applyraise(self):
		self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('alan', 'preciado', 50)
emp_2 = Employee('pluto', 'perez', 40)


#emp_1.raise_amount = 1.05 #This is the instance variable

#print(emp_1.__dict__)

#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

print(Employee.num_of_emps)