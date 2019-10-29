'''Insertion Sort

Sort by Building the final sorted list one item at a time.'''


def insertion_sort(arr):
	'''Sort by building the final sorted list one time at a time.'''

	'''if reverse:
		for i in range(len(arr) -1):
			while i >= 0:
				if arr[i] < arr[i+1]:
					arr[i], arr[i+1] = arr[i+1], arr[i]
				i -= 1'''
	
	for i in range(len(arr)-1):
		while i >= 0:
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
			i -= 1
	return arr


def insertion_hard(arr):
	for j in range(1, len(arr)):
		key = arr[j]
		i = j-1
		while i>=0 and arr[i] > key:
			arr[i+1] = arr[i]
			i -= 1
		arr[i+1] = key

	return arr


# TEST
if __name__ == "__main__":
	unsorted_list = [
			[1, 4],
			[99, 1],
			[99, 8, 13, 7],
			[2],
			[44, 88, 23, 9, 1, 7, 8],
			[1, 2, 3, 4, 5, 6, 7],
			[7, 6, 5, 4, 3, 2, 1]
	]

	for unsorted in unsorted_list:
		print(insertion_hard(unsorted)==insertion_sort(unsorted))
		print(insertion_sort(unsorted))
		print(insertion_hard(unsorted))
