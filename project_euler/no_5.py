"""Project Euler No.5

Smallest Multiple

2520 is the smallest number 
that can be divided by each of the numbers from 1 to 10 without any remainder.

Return the smallest positive number 
that is evenly divisible by all of the numbers from 1 to 20."""


def is_prime(val):
	"""Return True if val is prime or return False"""
	if val < 2:
		return False
	elif val == 2:
		return True
	else:
		for div in range(2, val//2 +1):
			if val % div ==0:
				return False
		return True




def smallest_multiple(end):
	"""Return smallest multiple that can be divided 
	by number between 1 to end"""

	primes = [i for i in range(1, end+1) if is_prime(i)]
	powers = [0 for _ in primes]
	count = 0
	result = 1

	for n in range(1, end+1):
		for i in range(len(primes)):
			while n % primes[i] ==0:
				n //= primes[i]
				count +=  1
			if powers[i] < count:
				powers[i] = count
			count = 0

	for i in range(len(primes)):
		for _ in range(powers[i]):
			result *= primes[i]

	return result



if __name__ == '__main__':
	end = int(input())
	print(smallest_multiple(end))


	

