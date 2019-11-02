def rotLeft(a, d):
	for x in range(d):
		a.append(a.pop(0))
	return a

rotLeft([1,2,3,4],2)