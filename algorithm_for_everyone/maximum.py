""" Maximum Number Finder

return Maximum number in given list of numbers"""


def maximum(arr):
	"""Return maximum from the given list"""

	maximum = 0
	for num in arr:
		if num > maximum:
			maximum = num

	return maximum



if __name__ == "__main__":
	arr = [2, 1, 99, 81, 4, 28, 59]
	print(maximum(arr))
	

