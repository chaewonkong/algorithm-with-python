"""피보나치 수

No. 2747
URL: https://www.acmicpc.net/problem/2747

첫째 줄에 n이 주어진다. n은 45보다 작거나 같은 자연수이다.
첫째 줄에 n번째 피보나치 수를 출력한다.
"""

def fib(n):
    "Return n-th Fibonacci number"

    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(n-1):
            a, b = b, a + b
        return a


if __name__ == "__main__":
    N = int(input())
    print(fib(N))