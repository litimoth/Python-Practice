# reference:  http://docs.python.org/library/timeit.html
import timeit


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
fn = 'primes_v01'
t = timeit.Timer(fn + '()', 'from __main__ import ' + fn)
print fn, "(): took", round((t.timeit(number=RUNS) / RUNS), 6), "seconds"
fn = 'primes_v02'
t = timeit.Timer(fn + '()', 'from __main__ import ' + fn)
print fn, "(): took", round((t.timeit(number=RUNS) / RUNS), 6), "seconds"
