"""Linear Search Algorithm in Python

1. Check each element of the given list sequentially 
until a match for the target value is found.
2. Return -1 if there is no matched element in the list."""


def linear_search(target, to_search):
	"""Return all the position of target value in to_search list"""

	result = []

	for i in range(len(to_search)):
		if to_search[i] == target:
			result.append(i)

	return result

target = 18
to_search = [3, 11, 29, 4, 18, 9, 6, 18, 18, 99]

print(linear_search(target, to_search))

