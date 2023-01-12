# super module runs with Python 3
# Developers and Managers are good examples of subclasses: Both have Employee attributes

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

#Subclasses: Developer, Employee
class Developer(Employee): #Inherit from Employee class (inherit all its functionality)
	raise_amt = 1.10

	# Use constructor to specify programming langauge, for example
	def __init__(self, first, last, pay, prog_lang):
		#Both ways work
		super().__init__(first, last, pay) # Let Employee class handle those arguments
		#Employee.__init__(self, first, last, pay)

		self.prog_lang = prog_lang

class Manager(Employee):
	#Pass list of employees he supervises
	def __init__(self, first, last, pay, employees=None): #Never pass mutable data types (like lists) as default main arguments. Hence the None
		super().__init__(first, last, pay) 
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_employes(self): #priunt employees he supervises
		for emp in self.employees:
			print('-->', emp.fullname())

dev_1 = Developer('Alan', 'Preciado', 500, 'Python')
dev_2 = Developer('Test', 'Employee', 300, 'Java')

mgr_1 = Manager('Sue', 'Smith', 900, [dev_1]) #This manager supervises dev_1

#is instance will tell us if an object is an instance of a class
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

#is subclass will tell us if a class is subclass of another
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))



