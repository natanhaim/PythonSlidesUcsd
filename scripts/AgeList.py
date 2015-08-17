D = {}
for person in range(3):
	name = raw_input("enter name: ")
	age = int(input("enter age: "))
	if name in D:
		D[name].append(age)
	else:
		D[name] = [age]
	print ""

for d in D:
	print d + "->" + str(D[d])