from collections import Counter

def ransom_note(magazine, rasom):
	# print(Counter(rasom))
	# print(Counter(magazine))
	# print(Counter(rasom)-Counter(magazine))
	if((Counter(rasom) - Counter(magazine)) == {}):
		print("Yes")
	else:
		print("No")