"""유턴 싫어"""


def isConnected(map, r, c):
    for i in range(r):
        for j in range(c):
            count = 0
            if map[i][j] == ".":
                if i-1 >= 0 and map[i-1][j] == ".":
                    count += 1
                if j-1 >= 0 and map[i][j-1] == ".":
                    count += 1
                if i+1 < r and map[i+1][j] == ".":
                    count += 1
                if j+1 < c and map[i][j+1] == ".":
                    count += 1
                if count < 2:
                    return 1
    return 0


if __name__ == "__main__":
    r, c = [int(i) for i in input().split()]

    map = []
    for i in range(r):
        map.append(input())
    print(isConnected(map, r, c))
