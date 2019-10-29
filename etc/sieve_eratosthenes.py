"""Sieve of Eratosthenes in Python

For given n, 
return a list contains only prime numbers below n"""


def sieve(n):
	"""return list of all primes less than equal to n"""
	primes = [1] * (n+1)
	primes[0], primes[1] = 0, 0
	for i in range(2, int(n**0.5)+1):
		if primes[i]:
			for j in range(2*i, n+1, i):
				primes[j] = 0
	return [idx for idx in range(n+1) if primes[idx] == 1]