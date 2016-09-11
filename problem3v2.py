topNumber = 60085147589
testList = [x for x in range(1,int(topNumber**0.5))]
factors = [number for number in testList if topNumber % number == 0]
finalCountdown = [factor for factor in factors[::-1] if len([test for test in range(1,factor) if factor % test == 0]) == 1]
print(max(finalCountdown))
