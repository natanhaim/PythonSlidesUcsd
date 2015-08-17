def Filter(s, c):
	hiScores = []
	for score in s:
		if score >= c:
			hiScores.append(score)
	return hiScores

scores = [75, 80, 93, 60, 72, 74]
cutoff = 75
print Filter(scores, cutoff)