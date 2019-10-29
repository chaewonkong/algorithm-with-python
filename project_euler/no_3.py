"""Project Euler no.3 in Python: Largest Prime Factor

Return largest prime factor of given val"""
import math


def is_prime(n):
	"""Return true if n is prime, false if n is not prime."""

	root = int(math.sqrt(n))

	if n <= 2:
		return True

	for i in range(2, root+1):
		if n % i ==0:
			return False
	return True


def largest_prime_factor(val, prime_max=2):
	"""Return largest prime factor of val with recursion"""

	if val < 2:
		return prime_max

	for n in range(2, val+1):
		if is_prime(n):
			if val % n == 0:
				prime_max = max(prime_max, n)
				break
				
	return largest_prime_factor(val//prime_max, prime_max)



val = 600851475143
print(largest_prime_factor(val))
			

