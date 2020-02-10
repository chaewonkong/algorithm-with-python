"""수 찾기

백준 1920번
URL: https://www.acmicpc.net/problem/1920
"""


def solution(population, targets):

    population.sort()
    n = len(population)
    ret = [1] * len(targets)

    # 이분탐색으로 풀면 logn. M개의 원소 100,000개 돌아간다고 가정하면 nlogn
    def bin_search(start, end, arr, target):
        mid = (start + end) // 2

        if start >= end:
            if arr[mid] == target:
                return True
            return False
        else:
            if arr[mid] > target:
                return bin_search(start, mid-1, arr, target)
            elif arr[mid] == target:
                return True
            else:
                return bin_search(mid+1, end, arr, target)

    for i in range(len(targets)):
        if not bin_search(0, n-1, population, targets[i]):
            ret[i] = 0
    return ret


if __name__ == "__main__":
    N = int(input())
    population = list(map(int, input().split()))
    M = int(input())
    targets = list(map(int, input().split()))
    for result in solution(population, targets):
        print(result)
