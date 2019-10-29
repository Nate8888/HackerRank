def miniMaxSum(arr):
	sortedArr = sorted(arr)
	print(sum(sortedArr[0:len(arr)-1]),sum(sortedArr[1:len(arr)]))