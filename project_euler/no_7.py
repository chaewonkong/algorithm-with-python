"""n-th Prime Number

From Project Euler no.7
Return n-th prime number starting from 2"""


def is_prime(val):
	"""Return True for prime number val and False for else"""

	sqrt = int(val**0.5)

	for i in range(2, sqrt+1):
		if val % i ==0:
			return False

	return True


def n_th_prime(n):
	"""Return n-th prime number starts from 2"""

	count = 0
	val = 2

	while count < n:
		if is_prime(val):
			count += 1
		val += 1

	return val - 1


# Test
print(n_th_prime(10001))