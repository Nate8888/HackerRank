def staircase(n):
	n += 1
	[print((n-1-i)*" "+i*"#") for i in range(1,n)]
staircase(28)