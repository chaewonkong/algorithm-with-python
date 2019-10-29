"""Fast A+B in Python

from BaekJoon Online Judge.

Using fast input and output, return A+B"""


import sys


testcase = int(sys.stdin.readline())


def fast_io(testcase):
	for _ in range(testcase):
		a, b = map(int, sys.stdin.readline().rstrip().split(' '))
		print(a+b)


fast_io(testcase)
