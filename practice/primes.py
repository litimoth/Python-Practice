# Version 1, super basic
primes = []
isPrime = False;

for i in range(2, 1000):
	isPrime = True;
	for j in range(2, i-1):
		if ((i % j) == 0):
			isPrime = False;
			break
	if (isPrime):
		primes.append(i)

print primes
