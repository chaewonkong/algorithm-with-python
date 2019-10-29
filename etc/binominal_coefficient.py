"""Binominal Coefficient in Python Algorithm

Using several different approaches"""


# Using Recursion
def pick_recursion(n, r):
    """Return number of possible combinations of selecting r number of items
    from n number of items: Using recursion"""

    if n == r:
        return 1
    elif r == 0:
        return 1
    else:
        return pick(n-1, r-1) + pick(n-1, r)


# Using Factorial
def pick_factorial(n, r):
    """Return number of possible combinations of selecting r number of items
    from n number of items: Using factorial"""

    def factorial(k):
        """Return factorial outcome with dynamic programming"""

        result = 1
        if k == 1:
            return 1
        elif k == 0:
            return 1
        else:
            for i in range(1, k+1):
                result *= i
            return result

    return factorial(n) // (factorial(n-r) * factorial(r))
    

# Using Dynamic Programming
def pick_dynamic(n, r):
    """Return number of possible combinations of selecting r number of items
    from n number of items: Using dynamic programming"""

    base = [[0 for _ in range(r+1)] for _ in range(n)]



# Test Block


print(pick_factorial(3, 2))