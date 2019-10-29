'''
문제 설명
유클리드 공간에서, 넓이가 N인 직사각형 두 변을 각각 w, h라 한다. 이때 가능한 w, h 중 |w - h|의 최솟값을 구하시오.

조건
사각형의 넓이 N (1 <= N <= 10^13), 변의 길이 w, h는 모두 자연수이다.

입력 형식
사각형 넓이 N을 표준 입력에서 읽는다.

출력 형식
|w - h|의 최솟값을 표준 출력에 쓴다.
'''

import math

N = int(input())
start = math.sqrt(N)
while start > 0:
    ret = N / int(start)
    if int(ret) == ret:
        print(int(ret) - int(start))
        break
    else:
        start -= 1