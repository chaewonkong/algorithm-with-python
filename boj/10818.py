# 백준 10818
# 최소, 최대
"""
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.
모든 정수는 -1,000,000보다 크거나 같고,
1,000,000보다 작거나 같은 정수이다.
"""
MAX_NUM = -1000000
MIN_NUM = 1000000

def get_min_max_num(arr):
    max_num = MAX_NUM
    min_num = MIN_NUM
    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return min_num, max_num

# 실행
if __name__ == "__main__":
    n = int(input())
    arr = [int(num) for num in input().split(" ")]
    result = ' '.join(map(str, get_min_max_num(arr)))
    print(result)
