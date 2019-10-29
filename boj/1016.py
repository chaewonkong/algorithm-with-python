"""제곱ㄴㄴ수

어떤 수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 제곱ㄴㄴ수라고 한다.
제곱수는 정수의 제곱이다.
min과 max가 주어지면, min과 max를 포함한 사이에 제곱ㄴㄴ수가 몇 개 있는지
출력한다.

[입력]
첫째 줄에 min과 max가 주어진다.
min은 1보다 크거나 같고, 1,000,000,000,000보다 작거나 같은 자연수이고,
max는 min보다 크거나 같고, min+1,000,000보다 작거나 같은 자연수이다.

[출력]
첫째 줄에 [min,max]구간에 제곱ㄴㄴ수가 몇 개인지 출력한다.
"""


def solution(minimum, maximum):
    is_sqr = [0] * 1000001
    # actual num = index of cache + minimum
    i = 2
    while i*i <= maximum:
        start = minimum // (i*i)
        if start < 1:
            start = 1

        j = start
        while i*i*j <= maximum:
            if i*i*j >= minimum:
                is_sqr[i*i*j-minimum] = 1
            j += 1
        i += 1
    return maximum-minimum+1-sum(is_sqr)


if __name__ == "__main__":
    MIN, MAX = map(int, input().split())
    print(solution(MIN, MAX))

# print(solution(1001000000, 1002000000))
