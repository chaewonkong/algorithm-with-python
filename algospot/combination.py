"""Combination Algorithm with Recursion
(ex 6.2)

With given n number of continuous integers starting from 0,
print all possible combinations of picking m items from given numbers.


INPUT
n, m(n >= m >= 0) are given in the first line, separated by whitespace.

OUTPUT
Make each combination an array, and print all possible combinations separated with comma.


EX INPUT
3 2

EX OUTPUT
[0, 1], [0, 2], [1, 2]
"""

def get_all_combinations(n, m):

    picked = []

    def pick(n, picked, m):
        """Return all possible combination of range(n) numbers 
        separating each array of combination by commas"""

        to_pick = m
        if to_pick == 0:
            print(picked)
            return
        smallest = 0 if not picked else picked[-1] +1
        for i in range(smallest, n):
            picked.append(i)
            pick(n, picked, (to_pick-1))
            picked.pop()
    
    pick(n, picked, m)
    return

if __name__ == "__main__":
    n, m = map(int, input().split())
    get_all_combinations(n, m)
