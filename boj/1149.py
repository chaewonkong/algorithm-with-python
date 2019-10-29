"""RGB 거리

백준 1149번

RGB거리에 사는 사람들은 집을 빨강, 초록, 파랑중에 하나로 칠하려고 한다. 
또한, 그들은 모든 이웃은 같은 색으로 칠할 수 없다는 규칙도 정했다. 
집 i의 이웃은 집 i-1과 집 i+1이다.

각 집을 빨강으로 칠할 때 드는 비용, 초록으로 칠할 때 드는 비용, 
파랑으로 드는 비용이 주어질 때, 모든 집을 칠할 때 드는 비용의 
최솟값을 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 집의 수 N이 주어진다. N은 1,000보다 작거나 같다. 
둘째 줄부터 N개의 줄에 각 집을 빨강으로 칠할 때, 초록으로 칠할 때, 
파랑으로 칠할 때 드는 비용이 주어진다. 
비용은 1,000보다 작거나 같은 자연수이다.

[출력]
첫째 줄에 모든 집을 칠할 때 드는 비용의 최솟값을 출력한다.

[예제 입력]
3
26 40 83
49 60 57
13 89 99

[예재 출력]
96
"""

# 재귀 호출 limit을 10**6으로 확대
import sys
sys.setrecursionlimit(10**6)

INF = 987654321


def minimum_cost(costs):

    N = len(costs)
    COLORS = len(costs[0])
    cache = [[-1 for _ in range(COLORS)] for _ in range(N)]

    def calc_cost(n, c):
        if n < 0:
            return 0
        elif cache[n][c] != -1:
            return cache[n][c]
        tmp = INF
        for color in range(COLORS):
            if color != c:
                tmp = min(tmp, calc_cost(n-1, color) + costs[n][c])
        cache[n][c] = tmp
        return tmp

    def nth_min_cost(n):
        return min(calc_cost(n, i) for i in range(3))

    return nth_min_cost(N-1)


if __name__ == "__main__":
    N = int(input())
    costs = []
    for i in range(N):
        temp_costs = [int(j) for j in input().split(" ")]
        costs.append(temp_costs)
    print(minimum_cost(costs))

# if __name__ == "__main__":
#     costs = [[26, 40, 83], [49, 60, 57], [13, 89, 99]]
#     print(minimum_cost(costs))
