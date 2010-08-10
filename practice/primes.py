# reference:  http://docs.python.org/library/timeit.html
import timeit

# globals
MIN = 2
MAX = 1000
RUNS = 10


# Version 1 - super basic, check remainder for all numbers to n-1
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
fn = 'primes_v01'
t = timeit.Timer(fn + '()', 'from __main__ import ' + fn)
print fn, "(): took", round((t.timeit(number=RUNS) / RUNS), 6), "seconds\n"
