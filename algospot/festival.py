"""Festival.py

Algospot.com Problem ID: FESTIVAL

커다란 공연장을 빌려 록 페스티벌을 개최하고자 한다. 
페스티벌은 여러날 동안 진행되며 하루에 한 팀의 밴드가 공연을 한다. 
현재 L개의 밴드 팀이 섭외되어, 최소 L일 간 페스티벌을 진행해야 한다.
공연장 대관료는 매일 상이하며, 일정을 잘 정해 하루당 평균 대관 비용을 최소로 하고자 한다. (대관료는 100 이하의 자연수)
10^-7 이하의 절대/상대 오차는 정답 처리된다.
(1 <= L <= N <= 1000)

[입력]
입력의 첫줄: 테스트 케이스의 수 C(C<= 100)
둘째줄: 대관 가능 일수 / 밴드 팀 수
셋째줄: 날짜별 대관 비용

[출력]
각 테스트 케이스별로 한 줄에 최소의 평균 대관 비용을 출력

[예제입력]
2
6 3
1 2 3 1 2 3 
6 2
1 2 3 1 2 3

[예제출력]
1.7500000000
1.5000000000
"""


def minAvgPrice(N, L, arrCost):
    """Return minumum average rental price per day"""

    MAX_PRICE = 100
    rentDays = L
    minAvg = MAX_PRICE + 1

    while rentDays <= N:
        start = 0
        end = rentDays
        eachAvg = sum(arrCost[start:end]) / rentDays
        minAvg = min(minAvg, eachAvg)
        while end < N:
            eachAvg += (arrCost[end] - arrCost[start]) / rentDays
            minAvg = min(minAvg, eachAvg)
            start += 1
            end += 1
        rentDays += 1
    
    return minAvg


if __name__ == "__main__": 
    # Number of Test Cases
    C = int(input())

    # Contain all results in arrResults list. 
    arrResults = []
    for i in range(C):
        N, L = map(int, input().split())
        arrResults.append(minAvgPrice(N, L, [price for price in map(int, input().split())]))

    for case in range(C):
        print(arrResults[case])
