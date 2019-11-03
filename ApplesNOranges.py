def countApplesAndOranges(s, t, a, b, apples, oranges):
	apples_on_home = 0
	oranges_on_home = 0
	apples = [apple+a for apple in apples]
	oranges = [orange+b for orange in oranges]
	for x in apples:
		if x>=s and x<=t:
			apples_on_home+=1
	for y in oranges:
		if y>=s and y<=t:
			oranges_on_home+=1
	print(apples_on_home)
	print(oranges_on_home)