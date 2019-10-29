"""Number of Trailing Zeros in N factorial(n!)"""

def count_trailing_zero(n):
    """Return number of zeros in n!"""

    cache = [-1] * (n+1)
    def count_times_div(n, div):
        """Return counts of how many times n could be divided by div"""
        
        if n % div != 0:
            return 0
        elif cache[n] != -1:
            return cache[n]
        else:
            return count_times_div(n//div, div) + 1
    
    # store counts multiples of 2, 5, 10
    count = 0
    for i in range(1, n+1):
        cache[i] = count_times_div(i, 5)
        count += cache[i]
        
    return count


if __name__ == "__main__":
    N = int(input())
    print(count_trailing_zero(N))