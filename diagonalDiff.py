def diagonalDifference(arr):
	left_diag = 0
	right_diag = 0
    # Write your code here
	for i in range(len(arr)):
		left_diag += arr[i][i]
		right_diag += arr[i][len(arr)-1-i]
	return abs(left_diag-right_diag)

print(diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]]))
# 11 2 4
# 4 5 6
# 10 8 -12