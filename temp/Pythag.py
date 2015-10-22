import math

def pythag(a, b):
	c = math.sqrt(a ** 2 + b ** 2)
	return c
	
side_a = input('enter side a: ')
side_b = input('enter side b: ')
side_c = pythag(side_a, side_b)
print 'side c is: ' + str(side_c)
