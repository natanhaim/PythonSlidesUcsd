def ex3(array, n):
	array.sort()
	return array[-n:]

test_scores = [75, 38, 92, 15, 94, 50, 88]
print ex3(test_scores, 4)