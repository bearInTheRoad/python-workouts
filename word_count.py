def word_count(path):
	chars_count = 0
	words = {}
	line_count = 0
	with open(path, 'r') as file:
		for line in file:
			line_count += 1
			chars_count += len(line)
			for word in line.split():
				words[word] = words.get(word, 0) + 1
	
	print(f'number of chars is {chars_count}')
	print(f'number of unique words is {len(words)}')
	print(f'number of words is {sum(words.values())}')
	print(f'number of lines is {line_count}')
			

if __name__ == '__main__':
	word_count('./wcfile.txt')
