"""Recursive Maximum Finder in Python

Return Maximum by Using Recursion of function in Python"""


def maximum_re(numbers):
	"""Return maximum of given numbers by recursion"""

	if len(numbers) ==1:
		return numbers[0]

	else:
		if numbers[0] < numbers[1]:
			numbers.pop(0)
		else:
			numbers.pop(1)

		return maximum(numbers)


