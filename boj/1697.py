"""
숨바꼭질

수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
"""

import sys
from collections import deque

input = sys.stdin.readline

# def find(n, k, cnt):
#     if n > k:
#         return cnt + (n-k)
#     elif n == k:
#         return cnt
#     else:
#         if k % 2 == 0:
#             if abs(k//2 - n) <= abs(k-n):
#                 k //= 2
#                 cnt += 1
#                 return find(n, k, cnt)
#             else:
#                 k -= n
#                 cnt += n
#                 return find(n, k, cnt)
#         else:
#             k -= 1
#             cnt += 1
#             return find(n, k, cnt)

MAX = 100001


def solution(n, k):
    q = deque([n])
    visit = [0] * MAX

    def nextPos(next, cur):
        if 0 <= next and next < MAX:
            if visit[next] == 0 or (visit[cur] + 1 < visit[next]):
                visit[next] = visit[cur] + 1
                q.append(next)

    while q:
        cur = q.popleft()
        if cur == k:
            return visit[cur]
        nextPos(cur - 1, cur)
        nextPos(cur + 1, cur)
        nextPos(cur * 2, cur)


if __name__ == "__main__":
    N, K = map(int, input().split())
    print(solution(N, K))





# 1. 더하기 혹은 빼기(n, k 비교로 알 수 있다) 
# 2. 나누기
# 기본 전제: k 값을 줄여 나가며 문제를 푼다