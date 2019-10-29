"""Shift Left

You are given two strings. 
In a single move, you can choose any of them, 
and delete the first (i.e. leftmost) character.

For Example:

By applying a move to the string "where", the result is the string "here".
By applying a move to the string "a", the result is an empty string "".
Implement a function that calculates the minimum number of moves 
that should be performed to make the given strings equal.

(ex)
"test", "west" => 2
"test", "yes" => 7
"b", "ab" => 1
"""


def shift_left(a, b):    
    list_a = [c for c in a]
    list_b = [c for c in b]
    list_a.reverse()
    list_b.reverse()
    count = 0
    
    for i in range(min(len(list_a), len(list_b))):
        if list_a[i] == list_b[i]:
            count += 1
        else:
            break
    return len(a) + len(b) -(2 * count)


for a, b in [("test", "west"), ("test", "yes"), ("b", "ab"), ("", "a")]:
    print(shift_left(a, b))
# print(shift_left("test", "yes"))


