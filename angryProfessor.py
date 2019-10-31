def angryProfessor(k, a):
	notLate = 0
	for x in a:
		if x <= 0:
			notLate += 1
	if notLate >= k:
		return "NO"
	return "YES"