"""
가장 긴 증가하는 부분 수열

Baekjoon Online Judge
ID: 11053
URL: https://www.acmicpc.net/problem/11053


수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 
가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

[입력]
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

[출력]
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
"""


def longest_subsequence(n, seq):

    dp = [0 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if seq[i] > seq[j] and dp[i] < dp[j]:
                dp[i] = dp[j]
        dp[i] += 1

    return max(dp)


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(longest_subsequence(N, A))


# TEST_CASE1 = [10, 20, 30, 40, 50]
# TEST_CASE2 = [90, 80, 70, 60, 50, 70, 90]
# TEST_CASE3 = [10, 20, 10, 30, 30, 20, 60]
# TEST_CASE4 = [10, 20, 10, 30, 20, 50]

# print(longest_subsequence(5, TEST_CASE1))
# print(longest_subsequence(7, TEST_CASE2))s
# print(longest_subsequence(7, TEST_CASE3))
# print(longest_subsequence(6, TEST_CASE4))
