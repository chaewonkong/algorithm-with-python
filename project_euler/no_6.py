"""Sum Square Difference

Project Euler No.6

For numbers in range(1, n+1),
(1) Sum of squares of the numbers
(2) Square of the sum of the numbers

Return (2) - (1)"""

import time


def sum_of_squares(end):
	"""Return sum of all squares of numbers in range(1, end+1)"""

	s = 0
	for i in range(1, end+1):
		s += (i**2)

	return s



def square_of_sum(end):
	"""Return square of sum of all numbers in range(1, end+1)"""

	s = int(0.5*end*(end+1)) ** 2

	return s


# Test

t1 = time.time()
print(square_of_sum(100) - sum_of_squares(100))
t2 = time.time()
print(t2-t1, " Sec")