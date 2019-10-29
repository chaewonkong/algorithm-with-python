"""1번


어떤 수를 서로 다른 소수 3개의 합으로 표현하는 경우의 수를 구하려 합니다. 예를 들어 33은 총 4가지 방법으로 표현할 수 있습니다.

3+7+23
3+11+19
3+13+17
5+11+17
자연수 n이 매개변수로 주어질 때, n을 서로 다른 소수 3개의 합으로 표현하는 경우의 수를 return 하는 solution 함수를 작성해주세요.

제한 조건
n은 1,000 이하인 자연수입니다.

입출력 예
n	return
33	4
9	0
입출력 예 설명
예시 #1
문제에 나온 예와 같습니다.

예시 #2
9는 서로 다른 세 소수의 합으로 나타낼 수 없습니다.
"""
def solution(n):
    ret = []
    cache = [0,0] + [1]*(n-1)
    for i in range(2,n+1):
        if cache[i]:
            for j in range(2*i, n+1, i):
                cache[j] = 0
    for i in range(2, n):
        target = n
        if cache[i] and target > i:
            target -= i
            for j in range(2, target):
                tmp = target
                if cache[j] and tmp > j and i != j:
                    tmp -= j
                    if cache[tmp] and i != tmp and j != tmp:
                        case = [i, j, tmp]
                        case.sort()
                        if case not in ret:
                            ret.append(case)

    return len(ret)

print(solution(33))