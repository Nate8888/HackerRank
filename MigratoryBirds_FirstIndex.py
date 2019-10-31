def migratoryBirds(arr):
	dictAll = {}
	for x in arr:
		dictAll[x] = dictAll.get(x)+1 if dictAll.get(x) else 1
	print("STOP\n\n")
	print(dictAll)
	return list(dictAll.keys())[list(dictAll.values()).index(max(dictAll.values()))]