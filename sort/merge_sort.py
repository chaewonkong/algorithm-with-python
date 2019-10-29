'''Merge Sort Algorithm in Python

Python algorithm that executes as follow:

1. Divide the unsorted list into n sublists each containing 1 element.
2. Repeatedly merge sublists to produce new sorted sublists
until there is only 1 sublist remaining.

Return the final existing list.'''


# def merge_sort(arr):
# 	"""Merge sort using divide and conquer"""

# 	length = len(arr)
# 	if length <= 1: # 탈출조건
# 		return
# 	mid = length // 2
# 	left = arr[:mid]
# 	right = arr[mid:]
# 	merge_sort(left)
# 	merge_sort(right)

# 	# Merge
# 	i, j, k = 0, 0, 0
# 	while i < len(left) and j < len(right):
# 		if left[i] < right[j]:
# 			arr[k] = left[i]
# 			i += 1
# 			k += 1
# 		else:
# 			arr[k] = right[j]
# 			j += 1
# 			k += 1
# 	while i < len(left):
# 		arr[k] = left[i]
# 		i += 1
# 		k += 1
# 	while j < len(right):
# 		arr[k] = right[j]
# 		j += 1
# 		k += 1

# 	return arr


def merge_sort(arr):
	"""Return sorted arr with merge sort algorithm"""
	def divide(lo, hi):
		"""Divide arr until the length of arr become 1"""
		if lo == hi:
			return
		mid = (lo + hi) // 2
		divide(lo, mid)
		divide(mid+1, hi)
		merge(lo, mid, hi)
	
	def merge(lo, mid, hi):
		"""Merge divided results by order"""
		left = lo
		right = mid + 1
		temp = []
		while left <= mid or right <= hi:
			if left <= mid and (right > hi or arr[left] < arr[right]):
				temp.append(arr[left])
				left += 1
			else:
				temp.append(arr[right])
				right += 1
		arr[lo:hi+1] = temp

	divide(0, len(arr) - 1)
	return arr


if __name__ == "__main__":
    arr = [int(i) for i in input(
                        "Input array of numbers separated by whitespaces-->"
                        ).split(' ')]
    print(merge_sort(arr))
