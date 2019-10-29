"""피보나치 수

No. 2749
URL: https://www.acmicpc.net/problem/2749

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 n이 주어진다. n은 1,000,000,000,000,000,000보다 작거나 같은 자연수이다.

[출력]
첫째 줄에 n번째 피보나치 수를 1,000,000으로 나눈 나머지를 출력한다.
"""

DIV = 1000000


def fib(n):
    SIZE = 2
    IDENTITY = [[1, 0], [0, 1]]
    BASE = [[1, 1], [1, 0]]

    def sqr_matrix_mul(mat_a, mat_b, size=SIZE):
        ret = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            for j in range(size):
                for k in range(size):
                    ret[i][j] += mat_a[i][k] * mat_b[k][j]
                    # 문제의 목적이 1000000로 나눈 나머지를 구하는 것이므로
                    # 1000000째 자리까지만 배열에 담아 추적
                    ret[i][j] = ret[i][j] % DIV

        return ret

    def generate(n):
        # fib(0)인 경우를 고려해 단위행렬로 초기화한다
        matrix = IDENTITY.copy()
        tmp = BASE.copy()
        k = 0

        while 2 ** k <= n:
            # 비트연산을 활용해 n에서 자리가 1인 자릿값을 찾는다
            if n & (1 << k) != 0:
                matrix = sqr_matrix_mul(matrix, tmp)
            k += 1
            # 매 번 tmp에는 tmp를 제곱한 값을 담으며, 2승씩 키워 나간다
            tmp = sqr_matrix_mul(tmp, tmp)

        return matrix

    return generate(n)[0][1]


if __name__ == "__main__":
    N = int(input())
    print(fib(N) % DIV)
