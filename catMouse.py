def catAndMouse(x, y, z):
	#Cat A, Cat B, Mouse C
	if abs(x-z) < abs(y-z):
		return "Cat A"
	elif abs(y-z) < abs(x-z):
		return "Cat B"
	else:
		return "Mouse C"