# to analyze a log file with ip address and return code

storage = {}

with open('./access.log', 'r') as file:
	for line in file:
		ip_addr, return_part = line.split('- -')
		print(ip_addr.strip())
		return_code_n_size = return_part.split('" ')[-1]
		return_code = return_code_n_size.split(" ")[0]
		print(return_code)
		
		storage[return_code] = storage.get(return_code, set())
		storage[return_code].add(ip_addr)

print(storage)
