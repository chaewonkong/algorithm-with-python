"""Is Palindrome in Python

Return true if given string s is palindrom, else return false."""

def is_palindrome(s, start, end):

    if end - start < 1:
        return True
    elif s[start] == s[end]:
        return is_palindrome(s, start+1, end-1)
    else:
        return False

s = input()
print(is_palindrome(s, 0, len(s)-1))
