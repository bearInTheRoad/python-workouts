def join_numbers(num_list):
	return ','.join([str(num) for num in num_list])

print(join_numbers(range(15)))

print([(x,y) for x in range(5) for y in range(5)])
