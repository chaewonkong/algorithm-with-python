
"""바둑이 포커
"""

# 입력은 항상 6개 출력은 항상 15개. 15개의 순서를 정렬하면 됨.


def card_sort(arr):
    return None


def solution(cards):
    pairs = []
    pair_dic = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    n = 6

    continuing = []
    same_number = []
    etc = []

    for i in range(n):
        for j in range(i+1, n):
            pairs.append(cards[i] + cards[j])
    for pair in pairs:
        if pair[0] < pair[2] and pair_dic[pair[0]] + 1 == pair_dic[pair[2]]:
            continuing.append(pair)
        elif pair[0] == pair[2]:
            same_number.append(pair)
        elif pair[0] > pair[2] and pair_dic[pair[0]] - 1 == pair_dic[pair[2]]:
            continuing.append(pair)
        elif pair[0] == 'f' or pair[2] == 'f':
            if pair[0] == '1' or pair[2] == '1':
                continuing.append(pair)
        else:
            etc.append(pair)

    for i in range(len(continuing)):
        for j in range(i+1, len(continuing)):
            if continuing[j][1] == continuing[j][3] and continuing[i][1] != continuing[i][3]:
                tmp = continuing[i]
                continuing[i] = continuing[j]
                continuing[j] = tmp
                continue
            nums_i = ([continuing[i][0], continuing[i][2]])
            nums_j = ([continuing[j][0], continuing[j][2]])
            if sorted(nums_j)[1] > sorted(nums_i)[1]:
                tmp = continuing[i]
                continuing[i] = continuing[j]
                continuing[j] = tmp
                continue
            if sorted(nums_j[0]) > sorted(nums_i)[0]:
                tmp = continuing[i]
                continuing[i] = continuing[j]
                continuing[j] = tmp
                continue
            if

    return continuing, same_number, etc


if __name__ == "__main__":
    cards = input().split(",")
    print(solution(cards))
