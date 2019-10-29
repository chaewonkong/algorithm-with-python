"""통계학

URL: https://www.acmicpc.net/problem/2108

수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 
통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 
단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
그 다음 N개의 줄에는 정수들이 주어진다. 
입력되는 정수의 절댓값은 4,000을 넘지 않는다.

[출력]
첫째 줄에는 산술평균을 출력한다. 
소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 
여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.
"""

import sys
K = 4000


class Stat:

    def __init__(self, N, maximum, array):
        self.length = N
        self.array = array
        self.maximum = maximum
        self.sorted_arr = []
        self.frequency_arr = []

    def counting_sort(self):
        cache = [0] * (self.maximum+1)
        ret = [0] * self.length

        for n in arr:
            cache[n] += 1
        self.frequency_arr = cache[:]

        for i in range(1, self.maximum+1):
            cache[i] += cache[i-1]

        idx = self.length - 1
        while idx >= 0:
            target = self.array[idx]
            ret[cache[target] - 1] = target
            cache[target] -= 1
            idx -= 1

        self.sorted_arr = ret[:]
        return ret

    def get_median(self):
        if not self.sorted_arr:
            self.counting_sort()
        return self.sorted_arr[self.length // 2]

    def get_avg(self):
        return sum(self.array) // self.length

    def get_range(self):
        if not self.sorted_arr:
            self.counting_sort()
        return self.sorted_arr[-1] - self.sorted_arr[0]

    def print_all(self):
        print("sorted_arr", self.sorted_arr)

    # def get_mode(self):
    #     if not self.sorted_arr:
    #         self.counting_sort()
    #     max_f = -1
    #     max_num = -1
    #     max_arr = []
    #     for i in range(self.maximum + 1):
    #         if self.frequency_arr[i] > max_f:
    #             max_f = self.frequency_arr[i]
    #             max_arr = [i]
    #         elif self.frequency_arr[i] == max_f:
    #             max_arr.append(i)
    #     if len(max_arr) > 1:
    #         return sorted(max_arr)[1]
    #     else:
    #         return max_num[-1]


if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(sys.stdin.readline().rstrip()))
    stat = Stat(N, 4000, arr)
    print("Avg", stat.get_avg())
    print("Med", stat.get_median())
    print("Range", stat.get_range())
    stat.print_all()
