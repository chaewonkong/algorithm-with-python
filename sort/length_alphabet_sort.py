"""Length - Alphabet Sorting Program

Firstly sort by length than sort by alphabet.
Primary sorting condition is length of element. 
Alphabet order is secondary."""


def sort_by_len_abc(arr):
	""" Return sorted list first by length then by abc order"""

	arr.sort()

	# Sort list ordered by length of element
	for i in range(len(arr)-1):
		while i >= 0:
			if len(arr[i]) > len(arr[i+1]):
				arr[i], arr[i+1] = arr[i+1], arr[i]
			i -= 1
	return arr


def sort_by_lambda(arr):
	"""Return sorted list by assigning key using lambda function""" 
	arr.sort(key=lambda x: (len(x), x))

	return arr

# Sample Case
unsorted = ['bbb', 'bbc', 'abc', 'aaaaa', 'c', 'aa', 'ab', 'ba', 'b']

print(sort_by_len_abc(unsorted))
print(sort_by_lambda(unsorted))