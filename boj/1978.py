"""Count Prime Numbers,
in Python

Baekjoon Online Judge, No.1978

Two lines of inputs all given.
number n given in the first line indicates number of total given numbers in the second line.
n number of numbers are given in the second line.
Return number of prime numbers of given numbers in the second line.
"""


def count_prime(arr):
	"""Return number of prime numbers in given array"""

	count = 0
	for i in arr:
		if i == 2:
			count += 1
		elif i > 2:
			div = 2
			while div <= i/2:
				if i % div == 0:
					count -= 1
					break
				else:
					div += 1
			count += 1


	return count


if __name__ == "__main__":
	n = int(input())
	arr = [int(i) for i in input().split(" ")]
	print(count_prime(arr))
