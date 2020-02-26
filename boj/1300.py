"""
백준 1300번
URL: https://www.acmicpc.net/problem/1300

세준이는 N*N크기의 배열을 만들었다. (배열의 방 번호는 1부터 시작한다.)

그 배열을 A라고 했을 때, 배열에 들어가는 수는 A[i][j] = i*j 이다.

세준이는 이 수를 일차원 배열 B에 넣으려고 한다. 그렇게 되면, B의 크기는 N*N이 될 것이다. 
그러고 난 후에, B를 오름차순 정렬해서 k번째 원소를 구하려고 한다.

N이 주어졌을 때, k번째 원소를 구하는 프로그램을 작성하시오.
"""


def solution(n, k):
    low = 1
    high = k
    ans = 0

    while low <= high:
        count = 0
        mid = (low + high) // 2

        for i in range(1, n+1):
            count += min(mid//i, n)

        if count >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    print(solution(n, k))
