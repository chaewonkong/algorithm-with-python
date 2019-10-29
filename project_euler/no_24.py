"""Project Euler No.24

A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def factorial(n):
	"""Return result of n factorial number"""

	if n == 1:
		return 1
	else:
		return n * factorial(n-1)


def lex_permutaion(arr, n):
	"""Return n-th number in lexicographic order of all numbers
	in input array"""

	k = len(arr)
	count = 1

	arr[]

