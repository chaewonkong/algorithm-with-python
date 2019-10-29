"""Find The Parity Outlier

from CodeWars
URL: https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

You are given an array (which will have a length of at least 3, 
but could be very large)
containing integers. 
The array is either entirely comprised of odd integers 
or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.

Examples:
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""

def find_outlier(integers):
    start = integers[0]
    end = integers[-1] 

    for i in range(1, len(integers)-1):
        temp = integers[i]
        if temp % 2 != start % 2 and temp % 2 != -start:
            if temp % 2 == end % 2 or temp % 2 == -end:
                return start
            return temp
    return end