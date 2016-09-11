primes = [2]
i = 3
def isPrime(number):
	token = 0
	for test in range(1,int(number**0.5)+1):
		if number % test == 0:
			token += 1
	if token != 1: return(False)
	else: return(True)
			
while len(primes)<10001:
	if isPrime(i): primes.append(i)
	i+=1
print(primes[10000])
