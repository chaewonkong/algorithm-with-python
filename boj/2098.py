"""외판원 순회(TSP)

1번부터 N번까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다.
(길이 없을 수도 있다) 이제 한 외판원이 어느 한 도시에서 출발해
N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는
순회 여행 경로를 계획하려고 한다. 단, 한 번 갔던 도시로는 다시 갈 수 없다.
(맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외)
이런 여행 경로는 여러 가지가 있을 수 있는데,
가장 적은 비용을 들이는 여행 계획을 세우고자 한다.

각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다.
W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다.
비용은 대칭적이지 않다. 즉, W[i][j] 는 W[j][i]와 다를 수 있다.
모든 도시간의 비용은 양의 정수이다. W[i][i]는 항상 0이다.
경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 이럴 경우 W[i][j]=0이라고 하자.

N과 비용 행렬이 주어졌을 때,
가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 도시의 수 N이 주어진다. (2 ≤ N ≤ 16) 다음 N개의 줄에는 비용 행렬이 주어진다.
각 행렬의 성분은 1,000,000 이하의 양의 정수이며, 갈 수 없는 경우는 0이 주어진다.
W[i][j]는 도시 i에서 j로 가기 위한 비용을 나타낸다.
항상 순회할 수 있는 경우만 입력으로 주어진다.

[출력]
첫째 줄에 외판원의 순회에 필요한 최소 비용을 출력한다.
"""

# 완전탐색으로 먼저 푼다
INF = 1000000000

curPos = 0
visited = 0
all_visited = 0
n = 0
cache = [[0 for _ in range(16)] for _ in range(1 << 16)]


def min_cost(curPos, visited):
    if visited == all_visited:
        if cost[curPos][0] == 0:
            return 987654321
        else:
            return cost[curPos][0]

    ret = cache[curPos][visited]

    if ret != 0:
        return ret

    ret = INF

    for i in range(1, n):
        if ((visited & (1 << i)) == 0) and (cost[curPos][i] != 0):
            ret = min(ret, min_cost(i, (visited | (1 << i))) + cost[curPos][i])
            cache[curPos][visited] = ret

    return ret


if __name__ == "__main__":
    n = int(input())
    all_visited = (1 << n) - 1
    cost = []
    for _ in range(n):
        cost.append([int(i) for i in input().split()])
    print(min_cost(0, 1))
