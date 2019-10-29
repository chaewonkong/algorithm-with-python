"""Quick Sort Algorithm in Python

1. Pick an element, called a pivot, from the array.
2. Partitioning: reorder the array so that 
all elements with values less than the pivot come before the pivot, 
while all elements with values greater than the pivot 
come after it (equal values can go either way). 
After this partitioning, the pivot is in its final position. 
3. Recursively apply the above steps to the sub-array of elements with smaller values
and separately to the sub-array of elements with greater values.
"""

import random


def quick_sort_easy(arr):
	""" Return sorted list by using quick sort algorithm"""

	n = len(arr)
	
	if n <= 1:
		return arr
	
	else:
		index = random.choice(range(n))
		pivot = arr.pop(index)
		smaller = []
		bigger = []

		for i in range(n-1):
			if arr[i] < pivot:
				smaller.append(arr[i])
			else:
				bigger.append(arr[i])

		return quick_sort_easy(smaller) + [pivot] + quick_sort_easy(bigger)



arr = [3, 19, 22, 48, 11, 1, 2, 5, 9, 8, 13, 22, 4, 7, 6, 18]
print(quick_sort_easy(arr))




	

