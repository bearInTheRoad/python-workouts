def get_final_line(path):
	with open(path, 'r') as file:
		print(file.readlines()[-1])

if __name__ == '__main__':
	get_final_line('./access.log')
