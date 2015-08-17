import math

def Pythag(a, b):
	c = math.sqrt(a ** 2 + b ** 2)
	return c
	
sideA = input("enter side a: ")
sideB = input("enter side b: ")
sideC = Pythag(sideA, sideB)
print "side c is: " + str(sideC)