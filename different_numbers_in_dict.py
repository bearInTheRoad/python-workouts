def how_many_different_numbers(*args):
	result = set(*args)
	return len(result)

numbers = [1,2,3,1,2,3,4,1]
print(how_many_different_numbers(numbers))
