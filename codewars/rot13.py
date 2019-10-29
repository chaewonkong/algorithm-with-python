"""ROT13

from CodeWars
URL: https://www.codewars.com/kata/rot13-1/train/python

ROT13 is a simple letter substitution cipher 
that replaces a letter with the letter 13 letters after it in the alphabet. 
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, 
they should be returned as they are. 
Only letters from the latin/english alphabet should be shifted, 
like in the original Rot13 "implementation".

Please note that using "encode" in Python is considered cheating.
"""

import string
from codecs import encode as _dont_use_this_

UPPER_START = 65
UPPER_END = 90
LOWER_START = 97
LOWER_END = 122

def rot13(message):
    ret = ""
    for l in message:
        if l.isalpha():
            order = ord(l) + 13
            if order > UPPER_END and order <= UPPER_END + 13 or order > LOWER_END:
                order -= 26
            l = chr(order)
        ret += l
    return ret

            
print(rot13("Test"))