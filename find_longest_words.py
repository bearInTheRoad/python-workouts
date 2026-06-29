import os

def find_longest_word(path):
	with open(path, 'r') as file:
		words = file.read().split()
		longest_word = max(words, key = len, default='')
	return longest_word

def find_all_longest_words(path):
	with os.scandir(path) as d:
		return {e.name: find_longest_word(e) for e in d if e.is_file()}

print(find_longest_word('./longest_word/science.txt'))
print(find_all_longest_words('./longest_word'))
