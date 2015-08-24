def ex1(s, e):
	if s <= 0 or e > 100 or s > e:
		print 'constraints: s>0, e<=100, s<e'
		exit()
	product = 1
	for i in range(s, e + 1):
		product *= i
	return str(product)
	
s = input('start: ')
e = input('  end: ')
print 'range product: ' + ex1(s, e)