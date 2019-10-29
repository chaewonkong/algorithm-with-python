"""동전 1

No. 2293
URL: https://www.acmicpc.net/problem/2293

n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 
이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 
그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

[입력]
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 
다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 
동전의 가치는 100,000보다 작거나 같은 자연수이다.

[출력]
첫째 줄에 경우의 수를 출력한다. 경우의 수는 2^31보다 작다.
"""
import sys


def solution(k, coins):
    n = len(coins)

    # Create 2D array for coins * k
    cache = [[0] * (k+1)] * (n+1)

    # Initiate padding to 1
    for i in range(1, n+1):
        cache[i][0] = 1

    for i in range(n):
        for j in range(1, k+1):
            if j >= coins[i]:
                cache[i][j] = cache[i][j-coins[i]] + cache[i-1][j]
            else:
                cache[i][j] = cache[i-1][j]
    return cache[-1][-1]


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().rstrip().split())
    coins = []

    for _ in range(n):
        tmp = int(sys.stdin.readline().rstrip())
        # value of coin cannot exceed k
        if tmp <= k:
            coins.append(tmp)

    print(solution(k, coins))
