def ex2(word):
	vowels = 0
	for letter in word.lower():
		if letter in ['a', 'e', 'i', 'o', 'u']:
			vowels += 1
	print word + ' has ' + str(vowels) + ' vowels'

	
ex2(raw_input('enter a word: '))