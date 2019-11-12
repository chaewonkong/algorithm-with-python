"""
소수 찾기

한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때,
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
17	3
011	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.
"""
import math


def solution(numbers):
    numbers = list(map(int, numbers))

    # All possible numbers
    permutations = []
    count = 0
    used = [0 for _ in range(len(numbers))]

    def search(selected, count_left):
        if not count_left:
            found = int("".join(map(str, selected)))
            if found not in permutations:
                permutations.append(found)
            return
        else:
            for i in range(len(numbers)):
                if used[i] == 0:
                    selected.append(numbers[i])
                    used[i] = 1
                    search(selected, count_left - 1)
                    selected.pop()
                    used[i] = 0

    def is_prime(n):
        if n < 2:
            return False
        for div in range(2, int(math.sqrt(n))+1):
            if n % div == 0:
                return False
        return True

    for i in range(1, len(numbers)+1):
        search([], i)
    # Get combinations
    for c in permutations:
        if is_prime(c):
            count += 1

    return count
