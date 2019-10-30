"""
듣보잡

Baekjoon Online Judge
ID: 1764
URL: https://www.acmicpc.net/problem/1764

김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때,
듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과,
N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.
이름은 띄어쓰기 없이 영어 소문자로만 이루어지며, 그 길이는 20 이하이다.
N, M은 500,000 이하의 자연수이다.

[출력]
듣보잡의 수와 그 명단을 사전순으로 출력한다.
"""
import sys

N, M = map(int, input().split())
ret = []
count = 0
not_heard_of = [sys.stdin.readline().rstrip() for _ in range(N)]
never_seen_before = [sys.stdin.readline().rstrip() for _ in range(M)]

not_heard_of.sort()
never_seen_before.sort()

i = 0
j = 0
ret = []
while i < N and j < M:
    if not_heard_of[i] == never_seen_before[j]:
        count += 1
        ret.append(not_heard_of[i])
        i += 1
        j += 1
    else:
        if not_heard_of[i] < never_seen_before[j]:
            i += 1
        else:
            j += 1

print(count)
while ret:
    print(ret.pop(0))
