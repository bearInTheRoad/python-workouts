import operator

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def calc2(expression):
	members = expression.strip().split(' ')
	
	if len(members) != 3:
		raise Exception('this only works with one operator and two numbers')
	
	operator, num1, num2 = members
	
	if operator not in ['+', '-', '*', '/', '%', '**']:
		raise Exception('this only works with basic 6 operators')

	if not is_float(num1) or not is_float(num2):
		raise Exception('this only works for float or interger numbers')

	return eval(f'{num1} {operator} {num2}')

def calc(expression):	
	members = expression.strip().split(' ')
	
	if len(members) != 3:
		raise Exception('this only works with one operator and two numbers')
	
	operand, num1, num2 = members

	mapping = {
		'+': operator.add,
		'-': operator.sub,
		'*': operator.mul,
		'/': operator.truediv,
		'**': operator.pow,
		'%': operator.mod
	}

	if operand not in ['+', '-', '*', '/', '%', '**']:
		raise Exception('this only works with basic 6 operators')

	if not is_float(num1) or not is_float(num2):
		raise Exception('this only works for float or interger numbers')
	
	return mapping.get(operand)(float(num1), float(num2))


test_cases = [
    ("+ 10 20", 30),         # Simple Addition
    ("- 50 10", 40),         # Simple Subtraction
    ("* 6 7", 42),           # Multiplication
    ("/ 10 4", 2.5),         # Division (float result)
    ("% 10 3", 1),           # Modulus
    ("** 2 3", 8),           # Exponentiation
    ("+ -5 10", 5),          # Negative numbers
    ("- 10 -5", 15),         # Subtraction with negative
    ("* 0 100", 0),          # Multiplication by zero
    ("/ 1 2", 0.5),          # Small division
    ("% 15 5", 0),           # Modulus with zero remainder
    ("** 5 2", 25),          # Standard power
    ("+ 1.5 2.5", 4.0),      # Floating point inputs
    ("/ -10 2", -5.0),       # Negative division
    ("** 9 0.5", 3.0),       # Square root via exponentiation
]

passed = 0
failed = 0

for expression, expected in test_cases:
    try:
        # Assuming your function is named 'calc' as per instructions
        result = calc(expression)
        
        # Using math.isclose for floats is usually better, 
        # but for these simple cases, direct comparison works.
        if result == expected:
            print(f"PASS  calc('{expression}') == {expected}")
            passed += 1
        else:
            print(f"FAIL  calc('{expression}') => {result}, expected {expected}")
            failed += 1
    except Exception as e:
        print(f"ERROR calc('{expression}') raised {e}")
        failed += 1

print(f"\n{passed} passed, {failed} failed")
