"""Project Euler No.4: Largest Palindrome Product

Return largest palindrome product below the given number"""


def max_palindrome(floor, ceiling):
	"""Return largest palindrome number of a * b,
	for int a, b above floor below ceiling"""

	a, b = ceiling -1, ceiling -1
	maximum = 0
	
	while a >= floor:
		while b >= floor:
			n = a * b
			n_reverse = int(str(n)[::-1])

			if n == n_reverse:
				maximum = max(maximum, n)
			b -= 1
		a -= 1
		ceiling -= 1
		b = ceiling -1

	return maximum


if __name__ == '__main__':
	floor, ceiling = map(int, input().split())
	print(max_palindrome(floor, ceiling))