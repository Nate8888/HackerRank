def checkMagazine(magazine, note):
	all_magazine_word = {}
	for each_word in magazine:
		if all_magazine_word.get(each_word):
			all_magazine_word[each_word] += 1
		else:
			all_magazine_word[each_word] = 1
	for each_word in note:
		if all_magazine_word.get(each_word):
			if all_magazine_word[each_word] < note.count(each_word):
				return "No"
		else:
			return "No"
	return "Yes"

print(checkMagazine(['two','times','three','is','not','four'],['two','times','two','is','four']))
# give me one grand today night
# give one grand today

# two times three is not four
# two times two is four