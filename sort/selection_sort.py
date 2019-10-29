'''Selection Sort

1. Divide input list into two sublists: sorted list and unsorted list
2. From unsorted list, find the minimum and exchange minimum with leftmost number
3. Move the sublist boundaries one element to the right'''


def select_sort(arr, reverse = False):
	'''Sort given list with selection sort algorithm'''

	arr = [[], arr]

	# Sort Descending
	if reverse == True:
		while arr[1]:
			for i in range(len(arr[1])):
				if arr[1][i] == max(arr[1]):
					arr[1][0], arr[1][i] = arr[1][i], arr[1][0]
			arr[0].append(arr[1].pop((0)))

	# Sort Ascending
	else:
		while arr[1]:
			for i in range(len(arr[1])):
				if arr[1][i] == min(arr[1]):
					arr[1][0], arr[1][i] = arr[1][i], arr[1][0]
			arr[0].append(arr[1].pop(0))

	return arr[0]


def select_hard(arr):
	"""Selection sort with in given list arr"""

	length = len(arr)

	for i in range(length):
		min_index = i
		for j in range(i, length):
			if arr[j] < arr[min_index]:
				min_index = j
		arr[i], arr[min_index] = arr[min_index], arr[i]

	return arr

if __name__ == "__main__":
	test = [int(i) for i in input().split(',')]
	
	print(select_hard(test))
	print(test)
	print(select_sort(test))
	print(test)
	
