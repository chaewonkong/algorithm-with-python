"""Number of Continuous Zeros

from BaekJoon Online Judge

Return continuous zeros from the right most unit for outcome of
N! (N factorial)
"""


def factorial(n):
	"""Return n factorial"""

	if n <= 1:
		return 1
	else:
		return n * factorial(n-1)


def zero_counter(n):
	"""Return number of continuous zeros from the right most"""

	fact_n = factorial(n)

	div = 10
	count = 0

	while fact_n % div ==0:
		count += 1
		div *= 10

	return count


print(zero_counter(10))



