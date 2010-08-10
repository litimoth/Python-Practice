MAX = 1000

# Version 1, super basic
def primes_v01():
	MIN = 2
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

# Version 2, still basic, but skip evaluating even numbers in both loops
def primes_v02():
	MIN = 3
	primes = [2]
	isPrime = False;
	for i in range(MIN, MAX, 2):
		isPrime = True;
		for j in range(MIN, i-1, 2):
			if ((i % j) == 0):
				isPrime = False;
				break
		if (isPrime):
			primes.append(i)
	return primes

# main()
print 'primes_v01(): ', primes_v01()
print 'primes_v02(): ', primes_v02()
