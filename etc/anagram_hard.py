"""Anagram in Python

Get two sorted arrays from two input strings by using merge sort.
Return boolean results: True for anagram, False for else."""


def merge_sort(arr):
    """Return sorted list from given raw array by using
    merge sort"""

    n = len(arr)
    if n <= 1:
        return
    mid = n //2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1
    
    # if remain items in left:
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    # If remain items in right:
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


def anagram(str1, str2):
    """Return True if str1 and str2 are anagrams, else return false
    by using merge sort"""

    arr1, arr2 = [l for l in str1], [m for m in str2]
    sorted_arr1 = merge_sort(arr1)
    sorted_arr2 = merge_sort(arr2)
    if sorted_arr1 == sorted_arr2:
        return True
    else:
        return False


if __name__ == "__main__":
    str1 = input()
    str2 = input()
    print(anagram(str1, str2))