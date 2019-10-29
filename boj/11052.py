# 카드 구매하기


def solution(n, p):
    p.insert(0, 0)
    d = [0] * (n+1)

    for i in range(1, n+1):
        for j in range(1, i+1):
            d[i] = max(d[i], d[i-j] + p[j])

    return d[n]


if __name__ == "__main__":
    n = int(input())
    p = [int(i) for i in input().split()]
    print(solution(n, p))
