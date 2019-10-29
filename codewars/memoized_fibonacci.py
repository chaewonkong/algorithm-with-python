"""Memoized Fibonacci

keep a cache data structure (most likely an associative array) 
where we will store the Fibonacci numbers as we calculate them. 
When a Fibonacci number is calculated, we first look it up in the cache, 
if it's not there, we calculate it and put it in the cache, 
otherwise we returned the cached number.
"""

def memoized(f):
    cache = {}
    def wrapper(k):
        v = cache.get(k)
        if v is None:
            v = cache[k] = f(k)
        return v
    return wrapper

@memoized
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# def fibonacci(n):
#     a, b = 1, 1
#     i = 1
#     while i < n:
#         i += 1
#         a, b = b, a + b
#     return a