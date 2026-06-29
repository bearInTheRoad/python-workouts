import os

ext_set = set()
for doc in os.listdir():
	ext = os.path.splitext(doc)[-1]
	ext_set.add(ext)
print(ext_set)
