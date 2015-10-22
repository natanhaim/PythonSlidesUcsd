def ex1(s, e):
	'''Compute product from s to e'''
	product = 1
	if (s > e) or (s < 1) or (e > 100):
		return 'error'
	for i in range(s, e + 1):
		product *= i
	return str(product)

s = input('start: ')
e = input('end: ')
print 'range product: ' + ex1(s, e)