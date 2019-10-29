"""Roman Numerals Encoder

from CodeWars
URL: https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python

Create a function taking a positive integer as its parameter 
and returning a string containing the Roman Numeral representation 
of that integer.

Modern Roman numerals are written by expressing each digit separately 
starting with the left most digit and skipping any digit with a value of zero. 
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 
2008 is written as 2000=MM, 8=VIII; or MMVIII. 
1666 uses each Roman symbol in descending order: MDCLXVI.

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

Remember that there can't be more than 3 identical symbols in a row.
"""
romans = \
        {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", \
        40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", \
        500: "D", 900: "CM", 1000: "M"}

def solution(n):
    romans = \
        {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", \
        40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", \
        500: "D", 900: "CM", 1000: "M"}
    keys = list(romans.keys())
    keys.reverse()

    def calc(n, ret):
        for div in keys:
            while n >= div:
                n -= div
                ret.append(div)
        return ret
    
    def encode(arr):
        ret = ""
        for num in arr:
            ret += romans[num]
        return ret
    
    return encode(calc(n, []))

print(solution(984))
print(solution(1000))
print(solution(1889))
print(solution(1989))