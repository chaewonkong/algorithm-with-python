def solution(arr, total):

    if len(arr) == 1:
        return sum(arr)
    arr.sort()
    print(arr)
    a = arr.pop(0)
    b = arr.pop(0)
    arr.append(a+b)
    total.append(a+b)
    return solution(arr, total)


if __name__ == "__main__":
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(solution(arr, [])+sum(arr))
