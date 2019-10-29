"""Amicalbe Numbers in Python

Project Euler No.21

d(n) is defined as the sum of proper divisors of n (n excluded).
If d(a) = b and d(b) = a where a != b, each a, b are called amicalbe numbers.

Return the sum of all amicalbe numbers under 10,000
"""

def d(n):
	"""Return sum of all proper divisors less than n)"""

	div = 2
	divisors = [1]

	if n == 1:
		return 0

	while div <= n//2:
		if n % div == 0:
			if div not in divisors:
				divisors = divisors + [div, n//div]
		div += 1

	return sum(divisors)


def sum_amicable_numbers(limit):
	"""Return sum of all amicalbe numbers under given limit"""

	results = []

	for n in range(2, limit+1): # exclude 1 for every d(n) >= 1 if n >1
		k = d(n)
		if k != n and d(k) == n:
			if n not in results:
				results = results + [n, k]

	return sum(results)


if __name__ == "__main__":
	print(sum_amicable_numbers(10000))
