"""정수 삼각형

from ACMICPC.NET(백준)
URL: https://www.acmicpc.net/problem/1932

       7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5

위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 


아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 
대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 
범위는 0 이상 9999 이하이다.

[입력]
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 
둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

[출력]
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.
"""
from sys import stdin


def max_path_sum(triangle):
    cache = [[0 for _ in row] for row in triangle]
    length = len(cache)

    cache[0] = triangle[0]
    for i in range(1, length):
        for j in range(i+1): 
            if i > j and j-1 >= 0:
                    cache[i][j] = max(cache[i-1][j-1], cache[i-1][j]) + triangle[i][j]
            elif i-1 >= 0 and j-1>= 0:
                cache[i][j] = cache[i-1][j-1] + triangle[i][j]
            elif i-1 >= 0:
                cache[i][j] = cache[i-1][j] + triangle[i][j]
    return max(cache[-1])


if __name__ == "__main__":
    N = int(input())
    triangle = list()
    for _ in range(N):
        triangle.append([int(i) for i in stdin.readline().rstrip().split()])
    print(max_path_sum(triangle))