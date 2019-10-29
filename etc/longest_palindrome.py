"""Longest Palindrome

From given string, return all longest palindromes in the string.

INPUT:
String length longer than equal to 0 is given in the first line.
String contains any kinds of character from UNICODE

OUTPUT:
Print list that contains all longest palindrome strings.

Note:
Empty string is considered as a palindrome.
"""


def longest_palindromes(s):
    ret = []

    for length in range(len(s), -1, -1):
        for start in range(len(s)-length+1):
            sub_str = s[start : start+length]
            if sub_str == sub_str[::-1]:
                ret.append(sub_str)
        if len(ret) > 0:
            break
    
    return ret


if __name__ == "__main__":
    s = input()
    print(longest_palindromes(s))