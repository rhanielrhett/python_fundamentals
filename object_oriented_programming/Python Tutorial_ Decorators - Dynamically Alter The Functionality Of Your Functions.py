# Decorators (9.8.18)

# NOTE: *args and **kwargs allow us to accept any 
# arbitrary number of positional or keyword arguments
# for our functions

# Decorators can be implemented as classes or functions 
# So either a class can decorate or a function

# Link to tutorial: https://www.youtube.com/watch?v=FsAPt_9Bf3U

# Common uses of decorators:
# 1. Timing how long each function runs
# 2. Keep track of a function being used, the arguments and kwarguments it is receiving (a logger)


#Function example
def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print('wraper executed this before {} '.format(original_function.__name__))
		return original_function(*args, **kwargs)
	return wrapper_function

#Class example (but functions are more common)
#class decorator_class(object):
	# def __init__(self, original_function):
	# 	self.original_function = original_function

	# #Like the wrapper function
	# def __call___(self, *args, **kwargs):
	# 	print('call method executed this before {}'.format(self.original_function.__name__))
	# 	return self.original_function(*args, **kwargs)	



#@decorator_function # --> This is the common syntax for decorators
@decorator_class
def display():
	print('display function ran')

# The @ is the same as saying
# display = decorator_function(display)

#decorated_display = decorator_function(display)
#decorated_display()

#@decorator_function
@decorator_class
def display_info(name, age):
	print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)

display()