"""Project Euler No.15

Lattice Path in Python

Starting in the top left corner of a 2×2 grid, 
and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

Return number of routes exists in 20*20 grid"""

def lattice_path(n):
	"""Return number of routes in n*n grid"""

	# 2D array of all possible points in given grid
	arr = [[0 for _ in range(n+1)] for _ in range(n+1)]

	# Each number in list means possible number of paths to that position
	for i in range(n+1):
		for j in range(n+1):
			if i <1 or j < 1:
				arr[i][j] = 1
			else:
				arr[i][j] = arr[i-1][j] + arr[i][j-1]

	# last number in last list: possible number of paths of final position
	return arr[-1][-1]

	


if __name__ == "__main__":
	# Test case for 2*2 grid
	print("Test case:\n2*2 grid =", lattice_path(2))
	# Actual case for 20*20 grid
	print("Answer:\n20*20 grid =", lattice_path(20))
