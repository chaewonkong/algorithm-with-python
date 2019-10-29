""""Find the missing letter

from Codewars
URL: https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python

Write a method that takes an array of consecutive (increasing) letters 
as input and that returns the missing letter in the array.

You will always get an valid array. 
And it will be always exactly one letter be missing. 
The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)
"""


def find_missing_letter(chars):
    N = len(chars)
    cache = [0 for _ in range(N)]
    cache[0] = ord(chars[0])
    
    for i in range(1, N):
        cache[i] = ord(chars[i])
        if cache[i] > cache[i-1] + 1:
            return chr(cache[i-1]+1)

