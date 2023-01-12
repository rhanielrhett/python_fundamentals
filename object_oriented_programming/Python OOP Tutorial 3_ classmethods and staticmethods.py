# Python object-oriented programming
# Tutorials by Corey Schafer

# To understand: Difference between class methods and static methods
# Regular method automatically takes the in the instance as the first argument
# How to take in the class as a first argument?? WE USE CLASS METHODS!

# Summarizing: Regular methods pass the instance as a first argument 'self', class methods pass the class as 'cls', and static method DON'T pass anything automatically
# Static methods behave like regular functions except we include the in classes because they have logical connection with the class. They can also be used as decorators
# Static methods should be defined when we don't access any instance or class within your function!

class Employee:

	#Class variable
	num_of_emps = 0
	raise_amount = 1.04 #this is an attribute to every instance of Employee

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

	#Basically we can use the decorator to pass a class as an argument instead of an instance
	@classmethod 
	def set_raise_amount(cls, amount): #instead of self
		cls.raise_amount = amount

	#Using class method as an alternative constructor
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay) #This line creates a new Employee object (using cls)

	@staticmethod
	def is_workday(day): # we just pass in the arguments that we want to work with
		if day.weekday() == 5 or day.weekday() == 6: # saturday or sunday
			return False
		return True

#emp_1 = Employee('alan', 'preciado', 50)
#emp_2 = Employee('pluto', 'perez', 40)

#Employee.set_raise_amount(1.05) # only need to pass amt as argument 
# This is the same as Employee.raise_amount = 1.05, but now we are using the classmethod set_raise_amount

#emp_1.raise_amount = 1.05 #This is the instance variable
#print(emp_1.__dict__)
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

#print(Employee.num_of_emps)

# Other common usages of classmethods is to create objects

emp_str_1 = "John-Doe-70"
emp_str_2 = "Steve-Smith-30"
emp_str_3 = "Jane-Doe-90"

#first, last, pay = emp_str_1.split('-')

#new_emp_1 = Employee(first, last, pay)

#Now people dont need to parse the string themselves, because we are using the from_string method
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

# STATIC METHODS
import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))
