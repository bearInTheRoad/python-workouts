def dictdiff(d1, d2):
	diff = {}
	for k in set([*d1.keys(), *d2.keys()]):
		d1_v = d1.get(k, None)
		d2_v = d2.get(k, None)
		if d1_v != d2_v:
			diff[k] = [d1_v, d2_v]
	return diff
			

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
assert dictdiff(d1,d1) == {}, 'not the same'

assert dictdiff(d1, d2) == {'c': [3,4]}, 'd1 d2 compare, not the same'

d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
assert dictdiff(d3, d4) == {'c': [None, 4], 'd': [3, None]}, 'd3 d4 compare wrong'

d5 = {'a':1, 'b':2, 'd':4}
assert dictdiff(d1, d5) == {'c': [3, None], 'd': [None, 4]}, 'd1 d5 compare wrong'
