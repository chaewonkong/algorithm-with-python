"""Sum of Prime Numbers in Given Range

Baekjoon Online Judge no.2581

Two numbers of integer input a, b are given, line by line.
Print sum of all prime numbers between a and b (a, b included) in the first line,
then print minimum of prime numbers between a and b.
if there is no prime number between a and b, print -1 
"""


def is_prime(n):
	"""Return boolean results for n.
	True for prime number, False for else."""

	if n < 2:
		return False
	elif n > 2:
		for div in range(2, n//2 + 1):
			if n % div == 0:
				return False
	return True


def min_and_sum_of_primes(minimum, maximum):
	"""Return sum of all prime numbers
	greater than equal to minimum, less than equal to maximum"""

	sum_of_primes = 0
	min_of_primes = maximum # Minimum of prime numbers should be less than maximum.
	for n in range(minimum, maximum+1):
		if is_prime(n):
			sum_of_primes += n
			min_of_primes = min(min_of_primes, n)
	if sum_of_primes == 0:
		return -1

	return sum_of_primes, min_of_primes


if __name__ == "__main__":
	M = int(input())
	N = int(input())

	results = min_and_sum_of_primes(M, N)

	if results == -1:
		print(results)
	else:
		print(results[0], results[1], sep="\n")




