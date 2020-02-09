"""공유기 설치
백준 2110번

URL: https://www.acmicpc.net/problem/2110
"""
from unittest import TestCase


def solution(c, houses):
    houses.sort()
    ans = 0

    def possible_number_of_routers(houses, distance):
        start = 0
        setted = 1
        for i in range(1, len(houses)):
            if houses[i] - houses[start] >= distance:
                setted += 1
                start = i
        return setted

    def bin_search(start, end):
        nonlocal ans
        mid = (start + end) // 2

        if start > end:
            return
        else:
            setted = possible_number_of_routers(houses, mid)
            if setted >= c:
                ans = mid
                return bin_search(mid+1, end)
            else:
                return bin_search(start, mid-1)

    bin_search(1, houses[-1] - houses[0])
    return ans


# Test Cases


# print(solution(3, [1, 2, 8, 4, 9])) # 3
# print(solution(4, [1, 2, 4, 5, 8, 11, 13])) # 3
# print(solution(5, [1, 2, 5, 4, 3])) # 1
# print(solution(2, [1, 2, 5, 4, 3])) # 4


if __name__ == "__main__":
    n, c = map(int, input().split())
    houses = []
    for _ in range(n):
        houses.append(int(input()))
    print(solution(c, houses))
