def dict_flip(inputs: dict):
	return {value: key for key, value in inputs.items()}

inputs = {'a': 1, 'b':2, 'c': 3}
print(dict_flip(inputs))
