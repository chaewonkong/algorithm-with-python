"""
적록색약

Baekjoon Online Judge
ID: 10026
URL: https://www.acmicpc.net/problem/10026

적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 
따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 
그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. 
(색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (
    빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. 
    (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 
적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.
"""
from collections import deque

D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n = int(input())
photo = [list(input()) for _ in range(n)]
checked = [[False for _ in range(n)] for _ in range(n)]


def bfs(r, c, color, red_green):
    q = deque()
    q.append((r, c))
    checked[r][c] = True

    while q:
        row, col = q.popleft()
        for i, j in D:
            nx, ny = row + i, col + j
            if (nx < 0 or nx >= n or ny < 0 or ny >= n) or checked[nx][ny]:
                continue
            if red_green and color == "B" and photo[nx][ny] != "B":
                continue
            if red_green and color != "B" and photo[nx][ny] == "B":
                continue
            if not red_green and photo[nx][ny] != color:
                continue
            q.append((nx, ny))
            checked[nx][ny] = True


count = 0

for i in range(n):
    for j in range(n):
        if checked[i][j] is False:
            bfs(i, j, photo[i][j], False)
            count += 1

print(count, end=" ")

count = 0
checked = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if checked[i][j] is False:
            bfs(i, j, photo[i][j], True)
            count += 1

print(count)
