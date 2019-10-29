"""Project Euler No.20

Factorial Digit Sum in Python

n! means n × (n − 1) × ... × 3 × 2 × 1.
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
"""


def factorial_digit_sum(n):
	"""Return sum of all digits in n!"""
	
	def factorial(n):
		"""Return n!"""
		if n == 1:
			return 1
		else:
			return n * factorial(n-1)

	val = factorial(n)
	result = 0

	while val >= 10:
		result += val % 10
		val //= 10
	return result + val


if __name__ == "__main__":
	n = int(input())
	print(factorial_digit_sum(n))