"""Fibonacci Algorithm 

Using Multiplication of Matrix"""


def fib(n):
    SIZE = 2
    IDENTITY = [[1, 0], [0, 1]]
    BASE = [[1, 1], [1, 0]]

    def sqr_matrix_mul(mat_a, mat_b, size=SIZE):
        ret = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            for j in range(size):
                for k in range(size):
                    ret[i][j] = mat_a[i][k] * mat_b[k][j]

        return ret

    def generate(n):
        matrix = IDENTITY.copy()
        tmp = BASE.copy()
        k = 0

        while 2 ** k <= n:
            if n & (1 << k) != 0:
                matrix = sqr_matrix_mul(matrix, tmp)
            k += 1
            # 매 번 tmp에는 tmp를 제곱한 값을 담으며, 2승씩 키워 나간다
            tmp = sqr_matrix_mul(tmp, tmp)

        return matrix

    return generate(n)[0][1]
