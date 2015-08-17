def GenKey(stringIn):
	stringIn = stringIn.lower()
	a = list(stringIn)
	a.sort()
	return "".join(a)

D = {}
print "processing word list..."
with open("wlist.txt") as f:
	for line in f:
		word = line.strip()
		k = GenKey(word)
		if k in D:
			D[k].append(word)
		else:
			D[k] = [word]
print "done"

word = raw_input("enter word: ")
print D[GenKey(word)]