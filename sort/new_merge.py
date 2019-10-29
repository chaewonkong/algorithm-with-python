"""Merge Sort Practice"""


def merge_sort(arr):
    
    def divide(lo, hi):
        
        mid = (lo + hi) // 2
        if lo == hi:
            return
        else:
            divide(lo, mid)
            divide(mid+1, hi)
        merge(lo, mid, hi)
    
    def merge(lo, mid, hi):

        left = lo
        right = mid + 1
        temp= []
        while left <= mid or right <= hi:
            if left <= mid and (right > hi or arr[left] < arr[right]):
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        arr[lo:hi+1] = temp

    divide(0, len(arr)-1)
    return arr


if __name__ == "__main__":
    test_arr = [3, 7, 9, 6, 44, 1, 8, 2, 13, 82, 64, 23, 21, 54]
    print(merge_sort(test_arr))
