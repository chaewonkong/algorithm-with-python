"""Binary Search in Python

For given sorted array, search and find Target and return offset of the target.
If target is not found, return -1.

INPUT:
Elements of ascending-sorted array is given in the first line, 
devided by whitespace.
Integer target is given in the second line.

OUTPUT:
Print offset of target if available, or print -1 if not available.
"""

'''
def binSearch(arr, T):
    """Return offset of T if T is in arr, or return -1"""
    
    start = 0
    mid = len(arr) // 2 - 1
    end = len(arr) - 1

    while end-start > 1:
        if arr[mid] > T:
            # Narrow the scope by discarding right elements
            end = mid
            mid = int((start+end) / 2)
        elif arr[mid] < T:
            # Narrow the scope by discarding left elements
            start = mid+1
            mid = int((start+end) / 2)
        else:
            # If arr[mid] == T
            return mid

    # Return result if result is found
    if arr[end] == T:
        return end
        
    #Return -1 for unavailable T
    else:
        return -1
'''

def binary_search(arr, target):

    def search(start, end):
        mid = (start + end) // 2
        if start == end:
            return -1 if arr[start] != target else start
        elif target > arr[mid]:
            return search(mid+1, end)
        else:
            return search(start, mid)
    
    return search(0, len(arr) -1)

    
if __name__ == "__main__":
    arr = [int(i) for i in input().split(" ")]
    target = int(input())
    print(binary_search(arr, target))
