primes = []
i = 0
def isPrime(number):
	token = 0
	for test in range(1,number):
		if number % test == 0:
			token += 1
	if token != 1: return(False)
	else: return(True)
			
while len(primes)<10001:
	if isPrime(i): primes.append(i)
	i+=1
print(primes[10000])
