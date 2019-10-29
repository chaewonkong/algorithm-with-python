"""Moving Average in Python

배열 A는 길이가 N인 실수 배열이다. 배열 A에 대해 M-이동평균을 구하라.
(1 <= M <= N)

[입력]
첫째 줄에 배열의 길이 N이 주어진다.
둘째 줄에 정수 M이 주어진다
셋째 줄에 배열 A의 원소가 공백으로 구분되어 주어진다.

[출력]
주어진 배열에 대해 M개의 값들의 이동평균을 순서대로 리스트에 저장해 출력한다.
"""


def movingAvg(length, M, arr):
    """Return list of M-moving-avg about arr"""

    results = []
    partialList = []

    for num in arr:
        if len(partialList) == M:
            results.append(sum(partialList)/M)
            partialList.pop(0)
            partialList.append(num)
        else:
            partialList.append(num)
    results.append(sum(partialList)/M)

    return results


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    A = [int(i) for i in input().split()]
    print(movingAvg(N, M, A))
