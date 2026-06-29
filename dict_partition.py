def dict_partition(d, f):
	dict1 = {}
	dict2 = {}
	for k in d:
		if f(k, d[k]):
			dict1[k] = d[k]
		else:
			dict2[k] = d[k]
	return (dict1, dict2)
		

# Helper functions for testing
def is_even_val(k, v): return v % 2 == 0
def key_starts_with_a(k, v): return str(k).lower().startswith('a')
def long_string_val(k, v): return len(str(v)) > 3

test_cases = [
    # (Input Dict, Input Function, Expected Output Tuple)
    
    # 1. Basic numbers: Partition by even values
    ({'a': 1, 'b': 2, 'c': 3, 'd': 4}, is_even_val, ({'b': 2, 'd': 4}, {'a': 1, 'c': 3})),
    
    # 2. Key-based logic: Keys starting with 'a'
    ({'apple': 10, 'banana': 20, 'art': 30, 'cat': 40}, key_starts_with_a, ({'apple': 10, 'art': 30}, {'banana': 20, 'cat': 40})),
    
    # 3. Empty dictionary
    ({}, is_even_val, ({}, {})),
    
    # 4. All True: All values meet the condition
    ({'b': 2, 'd': 4}, is_even_val, ({'b': 2, 'd': 4}, {})),
    
    # 5. All False: No values meet the condition
    ({'a': 1, 'c': 3}, is_even_val, ({}, {'a': 1, 'c': 3})),
    
    # 6. Mixed types: String length check
    ({1: 'dog', 2: 'elephant', 3: 'cat', 4: 'bird'}, long_string_val, ({2: 'elephant', 4: 'bird'}, {1: 'dog', 3: 'cat'})),
    
    # 7. Single element (True case)
    ({'alpha': 1}, key_starts_with_a, ({'alpha': 1}, {})),
    
    # 8. Single element (False case)
    ({'beta': 1}, key_starts_with_a, ({}, {'beta': 1}))
]

passed = 0
failed = 0

for (d, f, expected) in test_cases:
    try:
        # We use a copy of d to ensure the original isn't mutated during tests
        result = dict_partition(d.copy(), f)
        
        if result == expected:
            print(f"PASS  dict_partition with {f.__name__} on {d}")
            passed += 1
        else:
            print(f"FAIL  dict_partition with {f.__name__}")
            print(f"      Input: {d}")
            print(f"      Result:   {result}")
            print(f"      Expected: {expected}")
            failed += 1
    except Exception as e:
        print(f"ERROR dict_partition with {f.__name__} raised {e}")
        failed += 1

print(f"\n{passed} passed, {failed} failed")
