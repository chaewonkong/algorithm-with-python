"""Permutations

0부터 연속한 M개의 정수 중에서 N개를 순서 있게 뽑는 모든 경우의 수를 구하여라.
"""

M = 3
N = 3


def permutation(m, n):
    arr = [str(i) for i in range(m)]
    ret = []

    def calc(picked, topick):
        if topick == 0:
            ret.append("".join(picked[:]))
            return
        for i in range(n):
            if arr[i] not in picked:
                picked.append(arr[i])
                calc(picked, topick-1)
                picked.pop()
    calc([], n)
    return ret


print(permutation(M, N))
