"""Selection Sort in Python (from Algorithm for Everyone)"""


def select_sort(arr, reverse=False):
	"""Return sorted arr with selection sort algorithm"""

	if reverse:
		for i in range(len(arr)):
			for j in range(len(arr)):
				if max(arr[i:]) == arr[j]:
					arr[i], arr[j] = arr[j], arr[i]

	else:		
		for i in range(len(arr)):
			for j in range(len(arr)):
				if min(arr[i:]) == arr[j]:
					arr[i], arr[j] = arr[j], arr[i]

	return arr


arr = [3, 88, 4, 11, 25, 77, 34, 29, 6, 1, 2, 9, 33, 56, 5, 7]

print(select_sort(arr, reverse=True))
