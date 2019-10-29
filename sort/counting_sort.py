"""카운팅 정렬
"""

def counting_sort(arr, k):
    """Return sorted array by using counting sort. k is maximum number in array"""

    N = len(arr)
    cache = [0] * (k+1)
    ret = [0] * N

    for n in arr:
        cache[n] += 1
    for i in range(1, len(cache)):
        cache[i] += cache[i-1]
    i = N -1
    while i >= 0:
        num = arr[i]
        ret[cache[num]-1] = num
        cache[num] -= 1
        i -= 1
    return ret
