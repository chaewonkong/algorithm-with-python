'''
수열을 어떤 규칙에 의해 여러 가지 항으로 나누었을 때, 각각의 항으로 이루어진 수열을 군수열이라고 합니다.

무한수열 S = (1), (1, 2), (1, 2, 3), (1, 2, 3, 4).... 입니다. 이 수열의 규칙은 다음과 같습니다.

N 번째 군에는 1부터 N까지의 자연수가 크기 순서대로 있습니다.
수열의 k 번째 항은, 군에 상관없이 맨 앞부터 세기 시작합니다. 즉, 수열 S의 4번째 항은 1이 됩니다.
수 k가 주어질 때, 수열 S에서 k 번째 항의 수를 반환하는 solution 함수를 완성하세요.

제한사항
k는 50,000,000,000,000 이하의 자연수입니다.
입출력 예
k	result
4	1
10	4
입출력 예 설명
입출력 예 #1
k = 4 일때, (1), (1, 2), (1, 2 ...) 로 1을 반환합니다.

입출력 예 #2
k = 10 일때, (1), (1, 2), (1, 2, 3), (1, 2, 3, 4), (1, ... ) 로 4를 반환합니다.
'''


def solution(k):

    nxt = 0
    prev = 0
    i = 0
    while nxt < k:
        prev = nxt
        i += 1
        nxt = prev + i 
    return k - prev

print(solution(7))


# 성환
"""
MAX = int(5e13)
n_cache = [0]
n = 1
while True:
    n_cache.append(n_cache[-1] + n)
    n += 1
    if n_cache[-1] > MAX:
        break

def solution(k):
    n = 1
    while n_cache[n] < k:
        n += 1
    n -= 1
    return k - n_cache[n]
"""