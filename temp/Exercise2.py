def ex2(word):
	vowels = 0
	for letter in word:
		if letter in ['a', 'e', 'i', 'o', 'u']:
			vowels += 1
	print 'there are: ' + str(vowels) + ' vowels'
	
ex2(raw_input('enter a word: '))