"""Zebras and Ocelots
"""


def solution(creatures):
    n = len(creatures)
    # flag = True
    count = 0

    # while True:

    while True:
        count += 1
        while creatures[0] == "Z":
            creatures.pop(0)
        n = len(creatures)
        for i in range(n-1, -1, -1):
            if creatures[i] == "O":
                creatures[i] = "Z"
                for j in range(i+1, n):
                    creatures[j] = "O"
                if "O" not in creatures:
                    return count
                else:
                    break

##############################


    # 이진수의 덧셈 뺄셈이다.
if __name__ == "__main__":
    creatures = []
    num = int(input())
    for _ in range(num):
        creatures.append(input())
    # print(creatures)
    print(solution(creatures))
