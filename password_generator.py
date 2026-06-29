import random

def password_generator(candidates):
	
	def wrapper(num):
		return ''.join(random.choices(candidates, k=num))

	return wrapper


print(password_generator('abcdef')(5))
print(password_generator('123')(10))
