def sum_numbers(list_of_num: str)->int:
	numbers = (int(num) for num in list_of_num.split() if num.isdigit())

	return sum(list(numbers))

print(sum_numbers("10 abc 20 de44 30 55fg 40"))
