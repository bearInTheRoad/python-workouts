
def transform_value(inputs: dict):
	return {key: pow(int(value), 2) for key, value in inputs.items()}

inputs = {'a':1, 'b':2 , 'c':3}
print(transform_value(inputs))
print(transform_value(inputs) ==  {'a':1, 'b':4, 'c':9})

