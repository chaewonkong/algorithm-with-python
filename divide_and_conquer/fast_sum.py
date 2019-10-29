# Fast Sum n with divide and conquer

def fast_sum(n):
    if n == 1:
        return 1
    if n % 2 == 1:
        return fast_sum(n-1) + n
    return 2*fast_sum(n//2) + (n//2) * (n//2)


if __name__ == "__main__":
    print(fast_sum(int(input())))