def Repeats(grades):
	D = {}
	for g in grades:
		if g in D:
			D[g] += 1
		else:
			D[g] = 1
	return D

grades = ["A", "A+", "B", "B", "A", "C"]
rep = Repeats(grades)
for grade in rep:
    print grade + ": " + str(rep[grade])