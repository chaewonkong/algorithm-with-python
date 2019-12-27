# 숫자카드 2


def solution(cards, targets):
    target_dict = dict.fromkeys(targets, 0)
    for n in cards:
        if n in target_dict.keys():
            target_dict[n] += 1

    ret_str = " ".join(str(target_dict[i]) for i in targets)
    return ret_str


if __name__ == "__main__":
    N = int(input())
    cards = [int(n) for n in input().split()]
    M = int(input())
    targets = [int(m) for m in input().split()]
    print(solution(cards, targets))
