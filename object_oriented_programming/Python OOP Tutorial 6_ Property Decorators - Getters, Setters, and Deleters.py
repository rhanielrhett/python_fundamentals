
#How to use property decorator: allows to give class attributes getter, setter and deleter functionality
# We want to update the email automatically when either first name or last name change
# For this, getter and setters come in handy

class Employee:

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		#self.email = first + '.' + last + '@email.com'

	# In order to continue using email as an attribute, we can use a property decorator above the method
	@property #we are defining email as a method, but with this are able to access it like an attribute	
	def email(self):
		return '{} {}@email.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ') # split name into two spaces
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		print('Delete name')
		self.first = None
		self.last = None



emp_1 = Employee('Alan', 'Preciado', 50)

#emp_1.first = 'Jim'

emp_1.fullname = 'Luis Miguel' #In order to change first, last, email from here, we have to use a setter

print(emp_1.first)
print(emp_1.email) #Can access it like an atribute
print(emp_1.fullname)

del emp_1.fullname