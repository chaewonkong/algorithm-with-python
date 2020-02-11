"""색종이 만들기

백준 2630번
URL: https://www.acmicpc.net/problem/2630
"""


def solution(paper):

    n = len(paper)
    ans = [0, 0]

    def find(r, c, n):
        if n == 1:
            ans[paper[r][c]] += 1
            return
        start = paper[r][c]
        for i in range(n):
            for j in range(n):
                if paper[r+i][c+j] != start:
                    n //= 2
                    find(r, c, n)
                    find(r+n, c, n)
                    find(r, c+n, n)
                    find(r+n, c+n, n)
                    return
        ans[paper[r][c]] += 1
        return

    find(0, 0, n)
    return ans


if __name__ == "__main__":
    N = int(input())
    paper = []
    for _ in range(N):
        paper.append(list(map(int, input().split())))

    for ans in solution(paper):
        print(ans)
