"""
쉬운 계단 수
Baekjoon Online Judge
ID: 10844
URL: https://www.acmicpc.net/problem/10844

45656이란 수를 보자.

이 수는 인접한 모든 자리수의 차이가 1이 난다. 
이런 수를 계단 수라고 한다.

세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. 
(0으로 시작하는 수는 없다.)

[입력]
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

[출력]
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
"""
DIV = 1000000000

n = int(input())
arr = [1] * 10
arr[0] = 0

for i in range(1, n):
    temp = [0] * 10
    for (j, e) in enumerate(arr):
        if j == 0:
            temp[1] += e
        elif j == 9:
            temp[8] += e
        else:
            temp[j-1] += e
            temp[j + 1] += e

    arr = temp

print(sum(arr) % DIV)
