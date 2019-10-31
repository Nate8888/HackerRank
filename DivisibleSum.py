def divisibleSumPairs(n, k, ar):
	count = 0
	for i in range(len(ar)):
		for x in range(i+1,len(ar)):
			if (ar[i] + ar[x])%k == 0:
				count += 1
	return count