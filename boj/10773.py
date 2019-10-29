'''제로

https://www.acmicpc.net/problem/10773'''


def solution(arr):
    tmp = []
    for num in arr:
        if num != 0:
            tmp.append(num)
        else:
            tmp.pop()

    return sum(tmp)


if __name__ == '__main__':
    n = int(input())
    arr = list()
    for i in range(n):
        arr.append(int(input()))
    print(solution(arr))
