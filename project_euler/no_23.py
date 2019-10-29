"""Non-abundant Sums

Project Euler no.23

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two 
abundant numbers is 24.

By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed
as the sum of two abundant numbers is less than this limit.

Return sum of all the positive integers which cannot be written 
as the sum of two abundant numbers.
"""


def is_abundant(n):
	"""Return True if n is a abundant number, False otherwise."""

	result = 0
	div = 1

	while div <= n / 2:
		if n % div == 0 and n != div:
			result += div
		div += 1

	if n < result:
		return True
	return False


def non_abundant_sum(limit):
	"""Return sum of all numbers which cannot be written as the sum of 
	two abundant numbers"""

	# 1 if arr[i] is sum of two abundant numbers, 0 otherwise.
	boolean_arr = [0 for _ in range(limit+1)]
	length = len(boolean_arr)
	# Sum of all non_abundant_sum numbers
	result = 0

	for i in range(2, limit+1):
		j = i
		while (i * j) < length:
			if boolean_arr[i*j] == 1:
				j += 1
				continue
			else:
				if is_abundant(i*j):
					boolean_arr[i*j] = 1
				j += 1

	for l in range(length):
		if boolean_arr[l] == 0:
			result += l

	return result

# If a, b is abundant number, than a*b is also a abundant number!


if __name__ == "__main__":
	limit = 28123
	print(non_abundant_sum(limit))

	