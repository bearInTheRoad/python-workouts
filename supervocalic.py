def get_sv(path):
	with open(path, 'r') as file:
		words = file.read()
		
		return (
			word
			for word in words.lower().strip().split()
			if set(['a','e', 'u', 'i', 'o']) <= set(word)
		)


print(list(get_sv('./supervocalic.txt')))
