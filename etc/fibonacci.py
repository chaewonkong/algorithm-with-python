"""Fibonacci Algorithms in Python"""

def fib_recur(n):
    """return nth fibonacci number with recursion"""
    if n <1:
        return 0
    elif n <= 2:
        return 1
    return fib_recur(n-1) + fib_recur(n-2)

def fast_fib(n):
    """return nth fibonacci number within O(n)"""
    if n <1:
        return 0
    a, b = 1, 1
    count = 0
    while count < n-1:
        count += 1
        a, b = b, a+b
    return a