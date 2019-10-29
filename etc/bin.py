# Binary Search
class Error(Exception):
    pass


class UnsortedError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def binary_search(array, target):
    low = 0
    high = len(array)-1
    while (low <= high):
        mid = (low + high) // 2
        if array[mid] < target:
            low = mid+1
        elif array[mid] == target:
            return mid
        else:
            high = mid-1
    return -1


def test(n):
    arr = list()
    for i in range(n):
        arr.append(10*i)
    for i in range(n):
        print("n = ", i*10)
        assert binary_search(arr, 10*i) == i
        assert binary_search(arr, 10*i-5) == -1


if __name__ == "__main__":
    # n, target = map(int, input().split())
    # n = int(input())
    # test(n)
    arr = [int(i) for i in input().split()]
    target = int(input())
    print(binary_search(arr, target))
