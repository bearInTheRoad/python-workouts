def flatten(aList):
	
	return [e for cList in aList for e in cList]

print(flatten([[1,2], [3,4]]))
