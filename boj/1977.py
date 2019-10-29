"""완전제곱수

BOJ No. 1977

M과 N이 주어질 때 M이상 N이하의 자연수 중 완전제곱수인 것을 모두 골라 그 합을 구하고 
그 중 최솟값을 찾는 프로그램을 작성하시오. 
예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 완전제곱수는 
64,  81,  100 이렇게 총 3개가 있으므로 그 합은 245가 되고 이 중 최솟값은 64가 된다.

[예제입력]
60
100

[예제출력]
245
64
"""

import math

M = int(input())
N = int(input())
start = int(math.sqrt(M)) if math.sqrt(M).is_integer() else int(math.sqrt(M)) + 1
end = int(math.sqrt(N))
smallest = N
total = 0

for k in range(start, end+1):
    sqr = k ** 2
    if sqr < smallest:
        smallest = sqr
    total += sqr

if total:
    print(total)
    print(smallest)
else:
    print(-1)