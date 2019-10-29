"""Project Euler no.1: Multiples of 3 and 5 in Python

Retrun sum of multiples of 3 and multiples of 5,
while maximum multiple of 3 and maximum multiple of 5 is below 1000"""


def sum_multiples(n, k):
	"""Return sum of multiples of n, each multiple of n not exceed k"""

	if k%n ==0:
		end_pos = k//n-1
	else:
		end_pos = k//n

	sum_multiples = n * (0.5 * end_pos * (end_pos+1))

	return int(sum_multiples)

val = sum_multiples(3, 1000) + sum_multiples(5, 1000) -sum_multiples(15, 1000)
print(val)