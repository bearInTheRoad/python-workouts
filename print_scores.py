import os
import json
from pathlib import Path

def print_scores(path):
	for file in os.scandir(path):
		with open(file, 'r') as f:
			score = json.load(f)
			print(content)

print_scores('./scores')
