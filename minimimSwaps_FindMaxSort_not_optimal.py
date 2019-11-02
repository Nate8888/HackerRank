import math
def minimumSwaps(arr):
	currentMax = 0
	amount_of_swaps = 0
	compare = sorted(arr)
	while(arr!=compare):
		#Find the max value in the range so we can swap it later
		swapIndex = len(arr)-currentMax
		tempMax = max(arr[0:swapIndex])
		# If the max value is already in the last spot leave it there and increse the currentMax
		index_of_max_val = arr.index(tempMax)
		if  index_of_max_val == len(arr)-1-currentMax:
			currentMax += 1
			continue

		temporary_var_to_swap =  arr[swapIndex-1]
		arr[swapIndex-1] = tempMax
		arr[index_of_max_val] = temporary_var_to_swap
		amount_of_swaps += 1
		currentMax += 1
	return amount_of_swaps

print(minimumSwaps([3,2,17,4]))		 