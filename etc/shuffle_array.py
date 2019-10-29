"""Shuffle Array

Print Shuffled array only using random.random()
"""


import random

def shuffle_array(arr):
    """Return shuffled array from given arr"""

    rand_temp = [[random.random(), elm] for elm in arr]
    rand_temp.sort()
    results = [n for rand, n in rand_temp]

    return results


if __name__ == "__main__":
    arr = [i for i in range(1, 21)]
    print(shuffle_array(arr))
