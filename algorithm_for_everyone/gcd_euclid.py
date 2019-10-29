"""Calculating Greatest Common Divisor 
by Euclidean Algorithm in Python"""


def gcd(a, b):
	"""Return greatest common divisor by using Euclidean algorithm"""

	if b == 0:
		return a

	else:
		return gcd(b, a%b)