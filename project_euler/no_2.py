"""Project Euler no.2 in Python

Return sum of even numbers in fibonacci sequence.
Numbers in fibonacci do not exceed 4,000,000."""


def fib(n):
	"""Return n th number in fibonacci sequence"""

	a, b = 1, 1
	count = 0

	if n <= 2:
		return 1

	while count < n-1:
		a, b = b, a+b
		count += 1
	
	return a


def sum_even_fibonacci_numbers(n):
	"""Return sum of even numbers below n in fibonacci sequence"""

	result, k = 0, 1

	while True:
		if fib(3*k) <= n:
			result += fib(3*k)
			k +=1
		else:
			break

	return result

print(sum_even_fibonacci_numbers(4000000))