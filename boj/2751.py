"""수 정렬하기 2

백준 알고리즘 No.2751
URL: https://www.acmicpc.net/problem/2751

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

[입력]
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 
수는 중복되지 않는다.

[출력]
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""

import sys

def merge_sort(arr):
    """Sort array by using divide and conquer"""

    def divide(lo, hi):
        if lo == hi:
            return
        mid = (lo+hi) // 2
        divide(lo, mid)
        divide(mid+1, hi)
        merge(lo,mid, hi)

    def merge(lo, mid, hi):
        temp = []
        left = lo
        right = mid + 1
        while left <= mid or right <= hi:
            if left <= mid and (right > hi or arr[left] < arr[right]):
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        arr[lo:hi+1] = temp

    divide(0, len(arr)-1)
    return arr


if __name__ == "__main__":
    arr = []
    for _ in range(int(sys.stdin.readline().rstrip())):
        arr.append(int(sys.stdin.readline().rstrip()))
    for num in merge_sort(arr):
        print(num)
