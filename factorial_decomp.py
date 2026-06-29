from math import factorial, sqrt, ceil

def is_prime(n):
	if n in (1,2,3):
		return True
	if n == 4:
		return False
	a = 2
	while a * a <= n:
		if n % a == 0:
			return False
		a += 1
	return True

def max_exponantial(target, base):
	max_e = 1
	while target % base == 0:
		target //= base
		max_e += 1
	return max_e


def decomp(n):
	#your code here
	decomposing_list = []
	end_num = factorial(n)
	
	for i in range(2, n+1):
		if is_prime(i):
			decomposing_list.append((i, max_exponantial(end_num, i) - 1))
   
	return ' * '.join([f'{i}{"^" + str(max_e) if max_e > 1 else ""}' for i, max_e in decomposing_list])
	

print(decomp(5))
