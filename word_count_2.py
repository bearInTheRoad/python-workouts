def word_count(path):
	counts = {'characters': 0, 'words': 0, 'lines': 0}
	unique_words = set()

	for line in open(path, 'r'):
		counts['lines'] += 1
		counts['characters'] += len(line)
		counts['words'] += len(line.split())

		unique_words.update(line.split())

	counts['unique words'] = len(unique_words)
	for key,value in counts.items():
		print(f'{key}: {value}')

word_count('wcfile.txt')
