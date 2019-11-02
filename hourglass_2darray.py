def hourglassSum(arr):
	theSums = []
	for i in range(1,len(arr)-1):
		for y in range(1,len(arr)-1):
			tempQuan = arr[i-1][y-1] + arr[i-1][y] + arr[i-1][y+1] + arr[i][y] + arr[i+1][y-1] + arr[i+1][y] + arr[i+1][y+1]
			theSums.append(tempQuan)
	return (max(theSums))

hourglassSum([[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]])