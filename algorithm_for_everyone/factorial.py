"""Factorial Calculator in Python

Return outcome of n! (n factorial) for input(n)
by using recursion and by using dynamic programming"""


def fac_recur(n):
	"""Return result of n factorial by using recursion"""

	if n <= 1:
		return 1
	else:
		return n * fac_recur(n-1)


def factorial(n):
	"""Return result of n factorial by using dynamic programming"""

	result = 1
	for i in range(1, n+1):
		result *= i

	return result


if __name__ == "__main__":
	print(fac_recur(5))
	print(factorial(5))
	print(fac_recur(10))
	print(factorial(10))