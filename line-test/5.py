'''
연인 코니와 브라운은 광활한 들판에서 '나 잡아 봐라' 게임을 한다. 이 게임은 브라운이 코니를 잡거나 코니가 너무 멀리 달아나면 끝난다. 게임이 끝나는데 걸리는 최소 시간을 구하시오.

조건
코니는 처음 위치에서 1초 후 1만큼 움직이고, 이 후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1 만큼 움직인다. 즉, 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, ...이다.
브라운은 현재 위치 B에서 다음 순간 B - 1, B + 1, 2 * B 중 하나로 이동할 수 있다.
코니와 브라운의 위치 x는 0 <= x <= 200,000이다.
브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다.
입력 형식
표준 입력의 첫 줄에서 코니의 위치 C와 브라운의 위치 B를 공백으로 구분하여 순서대로 읽는다.

출력 형식
브라운이 코니를 잡을 수 있는 최소 시간 N초의 N을 표준 출력에 쓴다.
브라운이 코니를 잡지 못한 상태로 게임이 끝나면 표준 출력에 -1을 쓴다.
예
입력: 11 2
출력: 5

코니의 위치: 11, 12, 14, 17, 21, 26, ...
브라운의 위치: 2, 3, 6, 12, 13, 26, ...

브라운은 코니를 5초 만에 잡을 수 있다.
'''

def catch(C, B):
    ret = []
    def find(start, target, left, tmp):
        r = (start + 1, start * 2)
        if left == 0:
            if target == start:
                ret.append(start)
            return
        for case in r:
            tmp.append(case)
            find(case, target, left-1, tmp)
            tmp.pop()
    n = 0
    while n < 8:
        target = C + n*(n-1)//2
        find(B, target, n, [])
        n += 1
        if ret:
            return n
    return -1

    # n = 1
    # b, c = B, C
    # if b > c:
    #     while c <= b:
    #         n += 1
    #         b -= 1
    #         c = c + n*(n-1)//2
    # elif b == c:
    #     return 0
    # else:
    # return n


if __name__ == "__main__":
    C, B = map(int, input().split())
    print(catch(C, B))
        