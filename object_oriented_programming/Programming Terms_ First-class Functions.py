
#Understand: Functions can also be passed as arguments

# You can assign a function to a variable: without the () because that means 
# execute the function

# First aspects of first class functions: return functions!

def square(x):
	return x * x

def cube(x):
	return x * x * x

def my_map(func, arg_list): #with this, we can pass as argument any function we want
	result = []
	for i in arg_list:
		result.append(func(i))
	return result

squares = my_map(square, [1,2,3,4,5])

print(squares)

cubes = my_map(cube, [1,2,3,4,5])

print(cubes)