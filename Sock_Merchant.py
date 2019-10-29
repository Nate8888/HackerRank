amtsocks = int(input())
allsocks = input().split(" ")
pairs = 0
socksDict = {}
for x in allsocks:
	if x not in socksDict.keys():
		socksDict[x] = 1
	else:
		socksDict[x] += 1
		if(socksDict[x]==2):
			pairs+= 1
			socksDict[x] = 0
print(pairs)