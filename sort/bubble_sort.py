"""Bubble Sort in Python

Repeatidly swap adjacent items if they are in the wrong order, until no swaps are needed.
Return sorted array.
"""


def bubble_sort(arr):
	for i in range(len(arr)-1):
		j = len(arr) -1
		# Move smallest element in remainder to position i
		while j > i:
			if arr[j] < arr[j-1]:
				arr[j-1], arr[j] = arr[j], arr[j-1]
			j -= 1
			print(arr)
	return arr



if __name__ == "__main__":
	arr = [5, 4, 3, 2, 1]
	print(bubble_sort(arr))