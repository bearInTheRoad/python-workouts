def flatten_odd_ints(inputs):
	return [e
		for cList in inputs
		for e in cList
		if e%2 == 1]

test_cases = [
    # Basic flattening and odd filtering
    ([[1, 2, 3], [4, 5, 6]], [1, 3, 5]),           # Standard nested list
    ([1, [2, 3], [[4, 5], 6]], [1, 3, 5]),        # Deeply nested
    
    # String conversion logic
    (["1", "2", "3"], [1, 3]),                    # Strings that are integers
    (["10", "11", "abc", "13"], [11, 13]),        # Mixed strings (exclude non-numeric)
    ([[ "7", 8], ["9", "10"]], [7, 9]),           # Nested strings and ints
    
    # Edge cases: Types and Empty values
    ([], []),                                     # Empty list
    ([2, 4, 6, 8], []),                           # All even (should return empty)
    ([1.5, 3.0, 5.5, 7], [3, 7]),                 # Floats (3.0 is an odd int, others aren't)
    ([None, True, False, "5"], [5]),              # Mixed types (True/False are technically ints, but usually excluded)
    
    # Large numbers and signs
    ([-3, -2, -1, 0, 1], [-3, -1, 1]),            # Negative odd integers
    ([101, [202, [303]]], [101, 303]),            # Large odd numbers
]

passed = 0
failed = 0

# Note: The function name here is flatten_odd_ints as per your requirement
for inputs, expected in test_cases:
    try:
        # We use list(result) in case the function returns a generator
        result = list(flatten_odd_ints(inputs))
        if result == expected:
            print(f"PASS  flatten_odd_ints({inputs}) == {expected}")
            passed += 1
        else:
            print(f"FAIL  flatten_odd_ints({inputs}) => {result}, expected {expected}")
            failed += 1
    except Exception as e:
        print(f"ERROR flatten_odd_ints({inputs}) raised {type(e).__name__}: {e}")
        failed += 1

print(f"\n{passed} passed, {failed} failed")
