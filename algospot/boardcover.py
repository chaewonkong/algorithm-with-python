"""게임판 덮기 (난이도: 하)

ID: BOARDCOVER
URL: https://algospot.com/judge/problem/read/BOARDCOVER

H*W 크기의 게임판이 있습니다. 
게임판은 검은 칸과 흰 칸으로 구성된 격자 모양을 하고 있는데 
이 중 모든 흰 칸을 3칸짜리 L자 모양의 블록으로 덮고 싶습니다. 
이 때 블록들은 자유롭게 회전해서 놓을 수 있지만, 서로 겹치거나, 
검은 칸을 덮거나, 게임판 밖으로 나가서는 안 됩니다. 
위 그림은 한 게임판과 이를 덮는 방법을 보여줍니다.

게임판이 주어질 때 이를 덮는 방법의 수를 계산하는 프로그램을 작성하세요.

[입력]
입력의 첫 줄에는 테스트 케이스의 수 C (C <= 30) 가 주어집니다.
각 테스트 케이스의 첫 줄에는 2개의 정수 H, W (1 <= H,W <= 20) 가 주어집니다.
다음 H 줄에 각 W 글자로 게임판의 모양이 주어집니다. 
# 은 검은 칸, . 는 흰 칸을 나타냅니다. 
# 입력에 주어지는 게임판에 있는 흰 칸의 수는 50 을 넘지 않습니다.

[출력]
한 줄에 하나씩 흰 칸을 모두 덮는 방법의 수를 출력합니다.

[예제 입력]
3 
3 7 
#.....# 
#.....# 
##...## 
3 7 
#.....# 
#.....# 
##..### 
8 10 
########## 
#........# 
#........# 
#........# 
#........# 
#........# 
#........# 
########## 

[예제 출력]
0
2
1514
"""

import sys
sys.setrecursionlimit(100000)


def cover(H, W, board):
    count = 0
    
    def generate(H, W, board):
        """Generate graph, and left from given board arr"""
        left = 0
        graph = [[0 for _ in range(W)] for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if board[i][j] == "#":
                    graph[i][j] = 1
                else:
                    left += 1
        return graph, left
    
    
    if left % 3 != 0:
        return 0
    else:
        return count




if __name__ == "__main__":
    C = int(sys.stdin.readline().rstrip())
    ret = []
    for _ in range(C):
        H, W = map(int, sys.stdin.readline().rstrip().split())
        board = [sys.stdin.readline().rstrip() for _ in range(H)]
        ret.append(cover(H, W, board))
    for result in ret:
        print(result)
# 우선 0으로만 된 2차원 배열의 cache를 구성하고 덮어 나가는 과정에서 계속 기록하면 나가기.
# 기록하며 풀기 => 동적 계획법

"""
i,j => {
    1. (i, j), (i, j+1), (i+1, j)
    2. (i, j), (i+1, j), (i+1, j+1)
    3. (i, j), (i, j+1), (i+1, j+1)
    4. (i+1, j), (i+1, j+1), (i, j+1)
}

위 4가지의 경우의 수에 대해 모든 경우의 수를 탐색한다.
"""