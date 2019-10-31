def hurdleRace(k, height):
	cMax = max(height)
	if cMax > k:
		return cMax-k
	return 0