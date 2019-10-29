"""
Maximum Path Sum 1, from Project Euler no.18
"""


# Change given string into 2 dimensional array

arr = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

# 2D Array
arr_list = [string.split(' ') for string in arr.split('\n')]

# Change elements to integer and append padding 0 to both side and top.
for sub in arr_list:
	for i in range(len(sub)):
		sub[i] = int(sub[i])
	sub.append(0)
	sub.insert(0, 0)
arr_list.insert(0, [0, 0])


def max_path_finder(arr):
	"""Return path that sum of numbers in which is maximum"""

	cum_arr = [[0 for _ in sub] for sub in arr_list]
	
	# Contain sum of path in each element in list in cum_arr
	for i in range(1, len(cum_arr)):
		for j in range(1, len(cum_arr[i])-1):
			cum_arr[i][j] = max(cum_arr[i-1][j-1], cum_arr[i-1][j]) \
						+ arr[i][j]
	
	return max(cum_arr[-1])

if __name__ == "__main__":
	print(max_path_finder(arr_list))

