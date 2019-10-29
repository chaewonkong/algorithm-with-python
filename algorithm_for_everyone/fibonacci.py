"""Fibonacci n th Number Finder in Python

Return n th Fibonacci number by using,

1. Recursion
2. Dynamic Programming
3. Looping Technique
"""


def fib_recur(n):
	"""Return n th fibonacci number by using recursion"""
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib_recur(n-1) + fib_recur(n-2)


def fib_dynamic(n):
	"""Return n th fibonacci number by using dynamic programming"""

	
	fibs = [0 for _ in range(n+1)]
	fibs[0] = 0
	fibs[1] = 1

	for i in range(2, len(fibs)):
		fibs[i] = fibs[i-1] + fibs[i-2]

	return fibs[-1]


def fib(n):

	a, b = 1, 1
	count = 2

	for i in range(n-1):
		a, b = b, a+b

	return a
		


if __name__ == "__main__":
	i = 100
	#print(fib_recur(i))
	print(fib_dynamic(i))
	print(fib(i))