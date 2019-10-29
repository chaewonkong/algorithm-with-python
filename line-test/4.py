'''
위 그림과 같이 다양한 높이의 빌딩이 일직선 상에 세워져 있다. 이때 가로축은 일직선 상의 위치를, 세로축은 빌딩의 높이를 의미한다. 우리는 빌딩 사이에 지면과 평행하게 밧줄을 연결하려고 한다. 이 때 가장 긴 밧줄의 길이를 구하시오.

조건
밧줄은 한 빌딩의 꼭대기에서 시작하여 다른 빌딩에 연결한다.
두 빌딩 사이에 높이가 같거나 더 높은 다른 빌딩이 있다면 서로 연결할 수 없다.
위치 x1, x2인 두 빌딩 사이에 밧줄을 연결한다면 밧줄의 길이는 |x1 - x2|이다.
입력 형식
표준 입력의 첫째 줄에서 빌딩의 개수 N (2 <= N <= 1,000,000)을 읽는다.
둘째 줄 부터 N개의 줄에 걸쳐 빌딩의 높이 h (1 <= h <= 1,000,000)를 순서대로 읽는다. 이 때 x번째 줄에 입력한 빌딩의 위치는 x이다.
출력 형식
가장 긴 밧줄의 길이를 표준 출력에 쓴다.
'''
import sys

N = int(sys.stdin.readline().rstrip())
start = 0
second_tallest = 0
length = 0
max_length = 0
for _ in range(N):
    building = int(sys.stdin.readline().rstrip())
    length += 1
    if building >= start:
        max_length = max(max_length, length)
        second_tallest = 0
        start = building
        length = 0
    elif building < start:
        if second_tallest < building:
            second_tallest = building
            max_length = max(max_length, length)
print(str(max_length))
