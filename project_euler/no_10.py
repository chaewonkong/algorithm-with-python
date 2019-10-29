"""Sum of Primes, from Project Euler no.10

Return the sum of all primes below given value."""

import time


def is_prime(val):
	"""Return True for prime number val and False for else"""

	sqrt = int(val**0.5)

	for i in range(2, sqrt+1):
		if val % i ==0:
			return False

	return True


def eratos(limit):
	"""Return sum of all primes below limit by using Sieve of Eratosthenes"""

	arr = [1 for _ in range(limit)]
	arr[0] = 0

	for n in range(1, limit+1):
		for i in range(2, n//2+1):
			if n != i:
				if n//i ==0:
					arr[n-1] = 0
	print(arr)
	# 에라토스테네스의 채 아직 해결 안됨. 소수이면 1 아니면 0의 인덱스가 포함된 리스트.
	# 이 리스트들을 이용해 소수들의 합을 구해보자. 

	result = 0
	for j in range(len(arr)):
		if arr[j] == 1:
			result += (j+1)

	return result


def sum_of_primes(limit):
	"""Return sum of all primes below limit"""

	n = 2
	sum_prime = 0

	while n <= limit:
		if is_prime(n):
			sum_prime += n
		n += 1

	return sum_prime


# Test
print(sum_of_primes(2000000))


