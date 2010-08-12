# reference:  http://docs.python.org/library/timeit.html
import timeit
import math

# globals
MAX = 1000
RUNS = 10


# Version 1 - super basic, check remainder for all numbers to n-1
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


# Version 2 - still basic, but skip evaluating even numbers in both loops
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


# Version 3 - like v02, but only check up to the square root, as any
#			  divisor > sqrt(n), has a corresponding divisor < sqrt(n)
#    Now the question is, does computing the sqrt(n) add, or save time?
def primes_v03():
	MIN = 3
	primes = [2]
	isPrime = False;
	for i in range(MIN, MAX, 2):
		isPrime = True;
		sqrtOfI = int(math.ceil(math.sqrt(i))) + 1  #need +1 to avoid 25 -> 5 being skipped
		for j in range(MIN, sqrtOfI, 2):
			if ((i % j) == 0):
				isPrime = False;
				break
		if (isPrime):
			primes.append(i)
	return primes


# Version 4 - a basic seive program, only check even nums
def primes_v04():
	MIN = 3
	primes = [2]
	isPrime = False;
	for i in range(MIN, MAX, 2):
		isPrime = True;
		for j in primes:
			if ((i % j) == 0):
				isPrime = False;
				break
		if (isPrime):
			primes.append(i)
	return primes


# main()
FN = 'primes_v'
for n in range(1,5):
	fn = FN + (str(n) if (n >= 10) else ('0' + str(n)))
	t = timeit.Timer(fn + '()', 'from __main__ import ' + fn)
	time = (t.timeit(number=RUNS) / RUNS)
	print "%s(): took % 7.3f milliseconds" % (fn, time * 1000)

# Uncomment to print lists to check correctness
#print primes_v01()
#print primes_v02()
#print primes_v03()
#print primes_v04()
