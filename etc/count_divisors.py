"""Divisors Counter Algorithm in Python

Return number of divisors for given number n"""


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



