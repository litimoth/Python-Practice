MIN = 2
MAX = 1000

# Version 1, super basic
def primes_v01():
	primes = []
	isPrime = False;
	for i in range(MIN, MAX):
		isPrime = True;
		for j in range(MIN, i-1):
			if ((i % j) == 0):
				isPrime = False;
				break
		if (isPrime):
			primes.append(i)
	return primes

# main()
print primes_v01()
