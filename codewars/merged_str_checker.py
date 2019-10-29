"""Merged String Checker

from CodeWars
URL: https://www.codewars.com/kata/merged-string-checker/train/python

At a job interview, you are challenged to write an algorithm to check 
if a given string, s, can be formed from two other strings, part1 and part2.

The restriction is that the characters in part1 and part2 
are in the same order as in s.

The interviewer gives you the following example 
and tells you to figure out the rest from the given test cases.

(examples)
'codewars' is a merge from 'cdw' and 'oears':
    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears
"""


def is_merge(s, part1, part2):
    concat = part1 + part2
    if not s and not concat:
        return True
    if len(s) != len(concat):
        return False
    for l in s:
        if l not in concat:
            return False
    for c in concat:
        if c not in s:
            return False
    for i in range(1, len(part1)):
        if s.find(part1[i], s.find(part1[i-1])) == -1:
            return False
    for j in range(1, len(part2)):
        if s.find(part2[j], s.find(part2[j-1])) == -1:
            return False
    return True
    
print(is_merge('codewars', 'code', 'wars'))
    