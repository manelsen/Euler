topNumber = 600851475132143
testList = [x for x in range(1,int(topNumber**0.5))]
factors = [number for number in testList if topNumber % number == 0]
for factor in factors[::-1]:
	factorCount = []
	for test in range(1,factor):
		if factor % test == 0:
			factorCount.append(test)
	print(str(factor) + " - " + str(factorCount))
