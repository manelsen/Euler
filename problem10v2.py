primes = []
i = 1
def isPrime(number):
	token = 0
	for test in range(1,number):
		if number % test == 0:
			token += 1
		if test >= 10 and test >= number ** 0.5:
			break
	if token != 1: return(False)
	else: return(True)
			
while i < 10:
	if isPrime(i): primes.append(i)
	i+=1
print(sum(primes))
