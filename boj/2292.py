"""Length of Shorcut in Hive

Baekjoon Online Judge no.2292

Like given picture, each room has number written on it.
Number n is given as an input(1 <= n <= 1,000,000,000)
Starting from room number 1, find out the shortest path to reach room number n,
and return the number of rooms to be passed.
"""


def shortcut_count(n):
	"""Return number of rooms passed to reach nth room"""

	end = 1
	count = 0
	i = 0

	if n == 1:
		return 1

	while n > end:
		count += 1
		end += 6*i
		i += 1

	return count


if __name__ == "__main__":
	n = int(input())
	print(shortcut_count(n))

