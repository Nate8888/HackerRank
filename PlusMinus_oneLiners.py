def plusMinus(arr):
	pos = format(len([x for x in arr if x>0])/len(arr),'.6f')
	neg = format(len([x for x in arr if x < 0])/len(arr),'.6f')
	zero = format(1-(float(pos)+float(neg)),'.6f')
	[print(x) for x in [pos,neg,zero]]

plusMinus([-4,3,-9,0,4,1])