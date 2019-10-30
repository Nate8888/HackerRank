def extraLongFactorials(n):
	result = 1
	for x in range(1,n+1):
		result *= x
	print(result)

extraLongFactorials(25)