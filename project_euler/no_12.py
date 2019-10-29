"""Number of Divisors of Triangular Number (Project Euler no.12)

Return smallest triangular number that has at least k number of divisors."""


def count_divisors(n):
    """Return number of divisors for n"""

    div = 2
    count = 0
    result = 1

    while div <= n:
        while n % div ==0:
            n //= div
            count +=1
        result *= (count+1)
        div += 1
        count = 0

    return result


def minimum_num_divisors(limit):
	"""Return smallest triangular number 
	that has minimum n number of divisors"""

	n = 1
	count = 0

	while count <= limit:
		triangular = int(n*(n+1)*0.5)
		count = count_divisors(triangular)
		if count >= limit:
			return triangular
		n += 1

	return None


print(minimum_num_divisors(500))

